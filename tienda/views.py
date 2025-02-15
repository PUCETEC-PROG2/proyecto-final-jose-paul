from django.http import HttpResponse
from django.db.models import Q
from tienda.forms import ProductoForm, ClienteForm
from django.template import loader
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from .models import Carrito, Catalogo, Cliente, Compra, DetallesDeCompra, DetallesDeVenta, DetallesDelCarrito, Producto, Proveedor, Venta


# Create your views here.

class CustomLoginView(LoginView):
    template_name = "login_form.html"
    
    
def index(request):
    productos = Producto.objects.all().order_by('-precio')[:4]
    template = loader.get_template('index.html')
    return HttpResponse(template.render({
        'productos': productos,
    }, request))
    
def acerca_de(request):
    template = loader.get_template('acerca_de.html')
    return HttpResponse(template.render({}, request))
    
def clientes (request):
    clientes = Cliente.objects.all().order_by('nombres')
    template = loader.get_template('clientes.html')
    return HttpResponse(template.render({
        'clientes' : clientes
    }, request))
    
def buscar_productos(request):
    query = request.GET.get('q', '')  # Obtiene el término de búsqueda desde el input
    productos = Producto.objects.all()

    if query:
        productos = productos.filter(nombre__icontains=query)  # Filtra productos que contengan la búsqueda

    return render(request, 'busqueda.html', {'productos': productos, 'query': query})
    
def todas_las_categorias (request):
    productos = Producto.objects.all()
    template = loader.get_template('todas_las_categorias.html')
    return HttpResponse(template.render({
        'productos' : productos
    }, request))

def categoria_cuerdas (request):
    productos = Producto.objects.filter(categoria="C")
    template = loader.get_template('categoria_cuerdas.html')
    return HttpResponse(template.render({
        'productos' : productos
    }, request))

def categoria_percusion (request):
    productos = Producto.objects.filter(categoria="P")
    template = loader.get_template('categoria_percusion.html')
    return HttpResponse(template.render({
        'productos' : productos
    }, request))
    
def categoria_viento (request):
    productos = Producto.objects.filter(categoria="V")
    template = loader.get_template('categoria_viento.html')
    return HttpResponse(template.render({
        'productos' : productos
    }, request))
    
def categoria_teclado (request):
    productos = Producto.objects.filter(categoria="T")
    template = loader.get_template('categoria_teclado.html')
    return HttpResponse(template.render({
        'productos' : productos
    }, request))
    
def categoria_electronicos (request):
    productos = Producto.objects.filter(categoria="E")
    template = loader.get_template('categoria_electronicos.html')
    return HttpResponse(template.render({
        'productos' : productos
    }, request))
    
def informacion_instrumento(request, id_producto):
    producto = Producto.objects.get(pk = id_producto)
    template = loader.get_template('informacion_instrumento.html')
    context = {
        'producto': producto
    }
    return HttpResponse(template.render(context, request))

from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Cliente, Producto, Carrito, DetallesDelCarrito

def seleccionar_cliente(request):
    query = request.GET.get('q', '').strip()

    # Filtrar por nombre o cédula si se pasa un valor de búsqueda
    if query:
        clientes = Cliente.objects.filter(
            Q(nombres__icontains=query) | Q(apellidos__icontains=query) | Q(cedula__icontains=query)
        )
    else:
        clientes = Cliente.objects.all()
    print(f"Clientes encontrados: {clientes}")

    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        clientes_json = [
            {"id_cliente": cliente.id_cliente, "nombres": cliente.nombres, "apellidos": cliente.apellidos, "cedula": cliente.cedula}
            for cliente in clientes
        ]
        return JsonResponse({"clientes": clientes_json})

    return JsonResponse({"clientes": []})

def lista_productos(request):
    categoria = request.GET.get('categoria', '')

    if categoria:
        productos = Producto.objects.filter(categoria=categoria)
    else:
        productos = Producto.objects.all()

    productos_json = [
        {
            'id_producto': p.id_producto,
            'imagen': p.imagen.url if p.imagen else '',
            'nombre': p.nombre,
            'modelo': p.modelo,
            'marca': p.marca,
            'precio': str(p.precio),
            'categoria': p.categoria,
        }
        for p in productos
    ]

    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return JsonResponse({'productos': productos_json})

    return render(request, 'lista_productos.html', {'productos': productos})

@csrf_exempt
def actualizar_carrito(request):
    if request.method == "POST":
        producto_id = request.POST.get('producto_id')
        cantidad = int(request.POST.get('cantidad', 0))
        cliente_id = request.POST.get('cliente_id')

        cliente = get_object_or_404(Cliente, id_cliente=cliente_id)
        producto = get_object_or_404(Producto, id_producto=producto_id)

        carrito, _ = Carrito.objects.get_or_create(cliente=cliente, estado="activo")
        detalle, created = DetallesDelCarrito.objects.get_or_create(id_carrito=carrito, id_producto=producto)

        if cantidad > 0:
            detalle.cantidad = cantidad
            detalle.save()
        else:
            detalle.delete()

        total_carrito = sum(d.id_producto.precio * d.cantidad for d in DetallesDelCarrito.objects.filter(id_carrito=carrito))

        return JsonResponse({
            'producto_id': producto.id_producto,
            'cantidad': detalle.cantidad if cantidad > 0 else 0,
            'total_carrito': total_carrito,
        })

    return JsonResponse({'error': 'Método no permitido'}, status=400)

def obtener_carrito(request):
    cliente_id = request.GET.get('cliente_id')
    cliente = get_object_or_404(Cliente, id_cliente=cliente_id)
    carrito = get_object_or_404(Carrito, cliente=cliente, estado="activo")

    detalles = DetallesDelCarrito.objects.filter(id_carrito=carrito)
    detalles_json = [
        {
            'nombre': d.id_producto.nombre,
            'modelo': d.id_producto.modelo,
            'marca': d.id_producto.marca,
            'precio': d.id_producto.precio,
            'cantidad': d.cantidad,
        }
        for d in detalles
    ]

    return JsonResponse({'detalles': detalles_json})


@login_required
def add_producto(request):
    if request.method == "POST":
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('tiendamusical:index')
    else:
        form = ProductoForm()
    
    return render(request, 'producto_form.html', {'form': form})

@login_required
def add_cliente(request):
    if request.method == "POST":
        form = ClienteForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('tiendamusical:clientes')
    else:
        form = ClienteForm()
    
    return render(request, 'cliente_form.html', {'form': form})

@login_required
def edit_producto(request, id_producto):
    producto = Producto.objects.get(pk = id_producto)
    if request.method == "POST":
        form = ProductoForm(request.POST, request.FILES, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('tiendamusical:index')
    else:
        form = ProductoForm(instance=producto)
    
    return render(request, 'producto_form.html', {'form': form})

@login_required
def edit_cliente(request, id_cliente):
    cliente = Cliente.objects.get(pk = id_cliente)
    if request.method == "POST":
        form = ClienteForm(request.POST, request.FILES, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('tiendamusical:clientes')
    else:
        form = ClienteForm(instance=cliente)
    
    return render(request, 'cliente_form.html', {'form': form})

@login_required
def delete_producto(request, id_producto):
    producto = get_object_or_404(Producto, pk=id_producto)
    
    if request.method == "POST":
        producto.delete()
        return redirect('tiendamusical:index')

    return render(request, 'confirmar_eliminar_producto.html', {'producto': producto})

@login_required
def delete_cliente(request, id_cliente):
    cliente = get_object_or_404(Cliente, pk=id_cliente)
    
    if request.method == "POST":
        cliente.delete()
        return redirect('tiendamusical:clientes')

    return render(request, 'confirmar_eliminar_cliente.html', {'cliente': cliente})