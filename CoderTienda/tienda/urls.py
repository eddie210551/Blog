
from django.urls import path
from. import views


urlpatterns = [
    path('',views.Tienda, name="tienda"),
    path('pagos/',views.Pagos, name="Pagos"),
    path('carrito/',views.Carro, name="Carro")
]