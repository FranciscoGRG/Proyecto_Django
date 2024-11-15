from django.conf.urls.static import static
from django.urls import path

from .views import VRegistro, logear, cerrar_sesion

urlpatterns = [
    path('', VRegistro.as_view(), name='Autenticacion'),
    path('login', logear, name='login'),
    path('logout', cerrar_sesion, name='logout'),
]
