from django.contrib import admin

from .models import ShowDate, CinemaRoom, CinemaPremiere, Cast, Order


@admin.register(CinemaPremiere)
class PremiereAdmin(admin.ModelAdmin):
    list_display = ('film', 'release_date', 'duration')


@admin.register(Cast)
class CastAdmin(admin.ModelAdmin):
    list_display = ('actor_name', 'role', 'film')


@admin.register(CinemaRoom)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('room', 'number_of_tickets', 'price')


@admin.register(ShowDate)
class DateAdmin(admin.ModelAdmin):
    list_display = ('date', 'room', 'film', 'get_total_available_tickets')


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone_number', 'film', 'date')
