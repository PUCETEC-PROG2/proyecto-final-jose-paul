from django.urls import path
from . import views

app_name = 'tiendamusical'

urlpatterns = [
    path("", views.index, name="index"),
    path('login/', views.CustomLoginView.as_view(), name="login"),
    path('buscar_productos/', views.buscar_productos, name='buscar_productos'),
    path('clientes/', views.clientes, name='clientes'),
    path('todas_las_categorias/', views.todas_las_categorias, name='todas_las_categorias'),
    path('acerca_de/', views.acerca_de, name='acerca_de'),
    path("add_producto/", views.add_producto, name="add_producto"),
    path("add_cliente/", views.add_cliente, name="add_cliente"),
    path("edit_producto/<int:id_producto>/", views.edit_producto, name="edit_producto"),
    path("edit_cliente/<int:id_cliente>/", views.edit_cliente, name="edit_cliente"),
    path('eliminar_producto/<int:id_producto>/', views.delete_producto, name='eliminar_producto'),
    path('eliminar_cliente/<int:id_cliente>/', views.delete_cliente, name='eliminar_cliente'),
    path('categoria_cuerdas/', views.categoria_cuerdas, name='categoria_cuerdas'),
    path('categoria_viento/', views.categoria_viento, name='categoria_viento'),
    path('categoria_percusion/', views.categoria_percusion, name='categoria_percusion'),
    path('categoria_teclado/', views.categoria_teclado, name='categoria_teclado'),
    path('categoria_electronicos/', views.categoria_electronicos, name='categoria_electronicos'),
    path("<int:id_producto>/", views.informacion_instrumento, name="informacion_instrumento"),
    path('seleccionar_cliente/', views.seleccionar_cliente, name='seleccionar_cliente'),
    path('productos/', views.lista_productos, name='lista_productos'),
    path('actualizar_carrito/', views.actualizar_carrito, name='actualizar_carrito'),
    path('carrito/', views.obtener_carrito, name='obtener_carrito'),
] 