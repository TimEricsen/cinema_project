from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from .views import *

urlpatterns = [
    path('', main_page, name='main_page'),
    path('film/<str:film>', film_page, name='film_page'),
    path('film/<int:pk>/order', make_order, name='pre_order'),
    path('payment/<int:pk>', create_checkout_session, name='payment'),
    path('success/', success_payment, name='success'),
    path('cancel/', cancel_payment, name='cancel'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('registration/', register_user, name='registration')
]


if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns() + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
