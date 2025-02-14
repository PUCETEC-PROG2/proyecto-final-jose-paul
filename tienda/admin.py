from django.contrib import admin
from django.contrib import messages
from django.core.exceptions import ValidationError
from .models import Carrito, Catalogo, Cliente, Compra, DetallesDeCompra, DetallesDeVenta, DetallesDelCarrito, Producto, Proveedor, Venta

# Register your models here.
@admin.register(Carrito)
class CarritoAdmin(admin.ModelAdmin):
    pass

@admin.register(Catalogo)
class CatalogoAdmin(admin.ModelAdmin):
    pass

@admin.register(Cliente)
class ClientesAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        try:
            # Intentar guardar el objeto
            obj.save()
        except ValidationError as e:
            # Enviar el mensaje de error al admin
            messages.error(request, str(e))

@admin.register(Compra)
class ComprasAdmin(admin.ModelAdmin):
    pass

@admin.register(DetallesDeCompra)
class DetallesDeCompraAdmin(admin.ModelAdmin):
    pass

@admin.register(DetallesDeVenta)
class DetallesDeVentaAdmin(admin.ModelAdmin):
    pass

@admin.register(DetallesDelCarrito)
class DetallesDelCarritoAdmin(admin.ModelAdmin):
    pass

@admin.register(Producto)
class ProductosAdmin(admin.ModelAdmin):
    pass

@admin.register(Proveedor)
class ProveedoresAdmin(admin.ModelAdmin):
    pass

@admin.register(Venta)
class VentasAdmin(admin.ModelAdmin):
    pass