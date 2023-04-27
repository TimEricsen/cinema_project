from django.contrib.auth import logout
from django.shortcuts import render, redirect

from .services import context_for_main_page, context_for_film_page, context_for_order, get_session, context_for_successful_payment, context_for_canceled_payment
from .login_registration import login_context, register_context


def main_page(request):
    context = context_for_main_page()
    return render(request, 'main_page.html', context)


def film_page(request, film):
    context = context_for_film_page(film)
    return render(request, 'film_page.html', context)


def make_order(request, pk):
    context = context_for_order(pk)
    return render(request, 'pre_order.html', context)


def create_checkout_session(request, pk):
    session = get_session(request, pk)
    return redirect(session.url, 303)


def success_payment(request):
    context = context_for_successful_payment(request)
    return render(request, 'success_payment.html', context)


def cancel_payment(request):
    context = context_for_canceled_payment()
    return render(request, 'cancel_payment.html', context)


def user_login(request):
    context = login_context(request)
    return context


def user_logout(request):
    logout(request)
    return redirect('main_page')


def register_user(request):
    context = register_context(request)
    return context
