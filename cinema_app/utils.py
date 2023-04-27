import qrcode

from .models import Order


def create_qr_ticket(email, film, room, date, order_id):
    img = qrcode.make(f'{film} in room {room} on {date} for {email}')
    img_path = f'uploads/qr_tickets/{email[:-4]}_{order_id}.jpg'
    img.save(img_path)
    order = Order.objects.get(pk=order_id)
    order.qr_ticket = img_path
    order.save()
    return order.qr_ticket
