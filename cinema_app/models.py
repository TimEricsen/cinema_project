from django.db import models
from django.contrib.auth.models import User


class CinemaPremiere(models.Model):
    film = models.CharField(max_length=250, verbose_name='Film')
    description = models.TextField(verbose_name='Description')
    release_date = models.DateField(verbose_name='Release Date')
    duration = models.CharField(max_length=250, verbose_name='Duration')
    trailer = models.FileField(verbose_name='Trailer', upload_to='uploads/film_trailers/')
    image = models.ImageField(verbose_name='Film Poster', upload_to='uploads/film_posters/')

    class Meta:
        verbose_name = 'Film'
        verbose_name_plural = 'Films'

    def __str__(self):
        return self.film


class Cast(models.Model):
    actor_name = models.CharField(max_length=250, verbose_name='Actor Name')
    role = models.CharField(max_length=250, verbose_name='Role')
    image = models.ImageField(verbose_name='Actor image', upload_to='uploads/actors/')
    film = models.ForeignKey(CinemaPremiere, on_delete=models.CASCADE, verbose_name='Film', related_name='cast')

    class Meta:
        verbose_name = 'Cast'
        verbose_name_plural = 'Cast'

    def __str__(self):
        return f'{self.film} - {self.actor_name}'


class CinemaRoom(models.Model):
    room = models.IntegerField(verbose_name='Cinema Room')
    number_of_tickets = models.IntegerField(verbose_name='Number of Available tickets')
    price = models.IntegerField(verbose_name='Ticket Price')

    class Meta:
        verbose_name = 'Cinema Room'
        verbose_name_plural = 'Cinema Rooms'

    def __str__(self):
        return str(self.room)


class ShowDate(models.Model):
    date = models.DateTimeField(verbose_name='Show Date')
    room = models.ForeignKey(CinemaRoom, on_delete=models.CASCADE, verbose_name='Cinema Room', related_name='sdate')
    film = models.ForeignKey(CinemaPremiere, on_delete=models.CASCADE, verbose_name='Film', related_name='sdate')

    class Meta:
        verbose_name = 'Show Date'
        verbose_name_plural = 'Show Dates'
        unique_together = ('date', 'room')

    def __str__(self):
        return f'{self.film} on {self.date} in {self.room}'

    @property
    def get_total_available_tickets(self):
        total_count = self.room.number_of_tickets
        orders_count = self.order.all().count()
        return total_count - orders_count


class Order(models.Model):
    first_name = models.CharField(max_length=250, verbose_name='First Name')
    last_name = models.CharField(max_length=250, verbose_name='Last Name')
    phone_number = models.CharField(verbose_name='Phone Number')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='User', related_name='order')
    film = models.ForeignKey(CinemaPremiere, on_delete=models.CASCADE, verbose_name='Film', related_name='order')
    date = models.ForeignKey(ShowDate, on_delete=models.CASCADE, verbose_name='Show Date', related_name='order')
    is_paid = models.BooleanField(default=False, verbose_name='Is paid')
    qr_ticket = models.ImageField(verbose_name='QR ticket', upload_to='uploads/qr_tickets', blank=True, null=True)

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    def __str__(self):
        return f'{self.first_name} {self.last_name} - {self.film.film} on {self.date.date}'
