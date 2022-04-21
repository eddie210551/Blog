
from django.urls import path
from. import views


urlpatterns = [
    path('',views.Tienda, name="tienda"),
    path('carrito/pagos/',views.Pagos, name="Pagos"),
    path('carrito/',views.Carro, name="Carro"),
    path('login', views.login_request, name="Login")
]