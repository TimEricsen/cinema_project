import stripe

from django.urls import reverse
from django.conf import settings

from .tasks import send_email
from .forms import PreOrderForm
from .models import Cast, ShowDate, CinemaPremiere, Order


def context_for_main_page():
    context = {
        'title': 'Main Page',
        'films': CinemaPremiere.objects.all(),
        'show_dates': ShowDate.objects.all().order_by('date')[:7]
    }
    return context


def context_for_film_page(film):
    film = CinemaPremiere.objects.get(film=film)
    context = {
        'title': film,
        'film': film,
        'show_date': ShowDate.objects.filter(film=film),
        'cast': Cast.objects.filter(film=film)
    }
    return context


def context_for_order(pk):
    show_date = ShowDate.objects.get(pk=pk)
    context = {
        'title': 'Order' + show_date.film.film,
        'show_date': show_date,
        'film': show_date.film,
        'form': PreOrderForm()
    }
    return context


def get_session(request, pk):
    show_date = ShowDate.objects.get(pk=pk)
    stripe.api_key = settings.STRIPE_SECRET_KEY
    if request.method == 'POST':
        form = PreOrderForm(data=request.POST)
        if form.is_valid():
            new_order = Order.objects.create(**form.cleaned_data, date=show_date,
                                             film=show_date.film, is_paid=False,
                                             user=request.user)
            new_order.save()
            session = stripe.checkout.Session.create(
                payment_method_types=['card'],
                line_items=[{
                    'price_data': {
                        'currency': 'usd',
                        'product_data': {
                            'name': 'Ticket for cinema'
                        },
                        'unit_amount': int(show_date.room.price) * 100
                    },
                    'quantity': 1
                }],
                mode='payment',
                success_url=request.build_absolute_uri(reverse('success')),
                cancel_url=request.build_absolute_uri(reverse('cancel'))
            )
            return session


def context_for_successful_payment(request):
    order = Order.objects.filter(user=request.user).last()
    send_email.delay(order.user.email, order.film.film, order.date.room.room, order.date.date, order.pk)
    order.is_paid = True
    order.save()
    context = {
        'title': 'Payment complete',
        'order': order
    }
    return context


def context_for_canceled_payment():
    context = {
        'title': 'Payment was canceled'
    }
    return context
