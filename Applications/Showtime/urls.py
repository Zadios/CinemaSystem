from django.contrib import admin
from django.urls import path, include
from . import views
from .views import procesar_compra, listar_compra
app_name = "showtime_app"
urlpatterns = [
    path('compra/<int:show_id>/', listar_compra, name='listar_compra'),
    path('procesarCompra', procesar_compra, name='compra'),
]