from django.contrib import admin
from django.urls import path, include
from . import views

app_name = "showtime"
urlpatterns = [
    path('<int:film_id>/', views.horarios, name='horarios'),
    path('comprar_entradas/<int:show_id>/', views.comprar_entradas, name='comprar_entradas'),
    path('pago/', views.pago, name='pago'),
    path('confirmacion/<str:ticket_code>/', views.confirmacion, name='confirmacion'),
]