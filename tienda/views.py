from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect, render
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from .models import Carrito, Catalogo, Cliente, Compra, DetallesDeCompra, DetallesDeVenta, DetallesDelCarrito, Producto, Proveedor, Venta


# Create your views here.
def index(request):
    productos = Producto.objects.all().order_by('-precio')[:4]
    template = loader.get_template('index.html')
    return HttpResponse(template.render({
        'productos': productos,
    }, request))