from .utils import create_qr_ticket
from.models import ShowDate

from celery import shared_task
from cinema_project.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
from django.utils import timezone


@shared_task(bind=True)
def send_email(self, email, film, room, date, order_id):
    qr_ticket = create_qr_ticket(email, film, room, date, order_id)
    send_mail(
        subject=f'You have successfully bought a ticket for - {film}',
        message=f'Thanks for buying! Your session will be in room {room} on date {date}. Your ticket - http://127.0.0.1:8000/{qr_ticket}',
        from_email=EMAIL_HOST_USER,
        recipient_list=[email],
        fail_silently=False,
    )
    return 'Done!'


@shared_task(bind=True)
def checking_expired_sessions(self):
    show_dates = ShowDate.objects.all()
    for one_date in show_dates:
        if one_date.date < timezone.now():
            ShowDate.objects.get(pk=one_date.pk).delete()
        continue
    return 'Done!'
