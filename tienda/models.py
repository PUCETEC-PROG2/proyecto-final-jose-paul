# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models, connection


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Carrito(models.Model):
    id_carrito = models.AutoField(primary_key=True)
    id_cliente = models.ForeignKey('Cliente', models.DO_NOTHING, db_column='id_cliente')
    estado = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'carrito'
        verbose_name = "Carrito"           # Nombre singular en el admin
        verbose_name_plural = "Carritos"


class Catalogo(models.Model):
    id_catalogo = models.AutoField(primary_key=True)
    catalogo = models.CharField(max_length=30, blank=True, null=True)
    item = models.CharField(max_length=30, blank=True, null=True)
    id_raiz = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catalogo'
        verbose_name = "Catalogo"           # Nombre singular en el admin
        verbose_name_plural = "Catalogos"


class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    cedula = models.CharField(unique=True, max_length=10)
    nombres = models.CharField(max_length=40)
    apellidos = models.CharField(max_length=40)
    correo_electronico = models.CharField(unique=True, max_length=250)
    telefono = models.CharField(unique=True, max_length=10)
    direccion = models.CharField(max_length=300)
    fecha_de_registro = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cliente'
        verbose_name = "Cliente"           # Nombre singular en el admin
        verbose_name_plural = "Clientes"


class Compra(models.Model):
    id_compra = models.AutoField(primary_key=True)
    fecha_y_hora = models.DateTimeField(blank=True, null=True)
    total = models.DecimalField(max_digits=15, decimal_places=3)
    id_proveedor = models.ForeignKey('Proveedor', models.DO_NOTHING, db_column='id_proveedor')

    class Meta:
        managed = False
        db_table = 'compra'
        verbose_name = "Compra"           # Nombre singular en el admin
        verbose_name_plural = "Compras"


class DetallesDeCompra(models.Model):
    id_detalle_compra = models.AutoField(primary_key=True)
    id_compra = models.ForeignKey(Compra, models.DO_NOTHING, db_column='id_compra')
    id_producto = models.ForeignKey('Producto', models.DO_NOTHING, db_column='id_producto')
    cantidad = models.IntegerField()
    precio_unitario = models.DecimalField(max_digits=15, decimal_places=3)
    subtotal = models.DecimalField(max_digits=15, decimal_places=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'detalles_de_compra'
        verbose_name = "Detalles de compra"           # Nombre singular en el admin
        verbose_name_plural = "Detalles de compras"


class DetallesDeVenta(models.Model):
    id_detalle = models.AutoField(primary_key=True)
    id_venta = models.ForeignKey('Venta', models.DO_NOTHING, db_column='id_venta')
    id_producto = models.ForeignKey('Producto', models.DO_NOTHING, db_column='id_producto')
    cantidad = models.IntegerField()
    precio_unitario = models.DecimalField(max_digits=15, decimal_places=3)
    subtotal = models.DecimalField(max_digits=15, decimal_places=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'detalles_de_venta'
        verbose_name = "Detalles de venta"           # Nombre singular en el admin
        verbose_name_plural = "Detalles de ventas"


class DetallesDelCarrito(models.Model):
    id_detalle_carrito = models.AutoField(primary_key=True)
    id_carrito = models.ForeignKey(Carrito, models.DO_NOTHING, db_column='id_carrito')
    id_producto = models.ForeignKey('Producto', models.DO_NOTHING, db_column='id_producto')
    cantidad = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'detalles_del_carrito'
        verbose_name = "Detalles del carrito"           # Nombre singular en el admin
        verbose_name_plural = "Detalles de los carritos"


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'

class Producto(models.Model): 
    id_producto = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    marca = models.CharField(max_length=20)
    modelo = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=300)
    precio = models.DecimalField(max_digits=15, decimal_places=2)
    stock = models.IntegerField()
    
    P_CATALOGO = {
        ('C', 'Cuerdas'),
        ('V', 'Viento'),
        ('P', 'Percusión'),
        ('T', 'Teclado'),
        ('E', 'Electrónicos'),
    }
    categoria = models.CharField(max_length=50, choices=P_CATALOGO)
    imagen = models.ImageField(upload_to="proyecto_images", blank=True, null=True)  # Permitir que sea opcional
    fecha_de_creacion = models.DateField()

    def __str__(self):
        return f'{self.nombre}'

    class Meta:
        managed = False
        db_table = 'producto'
        verbose_name = "Producto"           # Nombre singular en el admin
        verbose_name_plural = "Productos"

    def save(self, *args, **kwargs):
        # Guardar el producto primero para asegurar que la imagen esté disponible en el sistema de archivos
        super(Producto, self).save(*args, **kwargs)

        # Obtener la URL de la imagen si está presente
        imagen_url = self.imagen.url if self.imagen and self.imagen.name else ''

        # Llamar al procedimiento almacenado
        with connection.cursor() as cursor:
            print(self.nombre, self.descripcion, self.categoria)
            cursor.execute('CALL gestionar_producto(%s, %s, %s, %s, %s, %s, %s, %s, %s)', [
                self.id_producto, 
                self.nombre, 
                self.descripcion, 
                self.precio, 
                self.stock, 
                self.categoria, 
                self.marca, 
                imagen_url,  # Aquí está corregido
                self.modelo,
            ])



class Proveedor(models.Model):
    id_proveedor = models.AutoField(primary_key=True)
    cedula = models.CharField(unique=True, max_length=10)
    nombres = models.CharField(max_length=40)
    apellidos = models.CharField(max_length=40)
    telefono = models.CharField(max_length=10)
    correo_electronico = models.CharField(unique=True, max_length=250)
    direccion = models.CharField(max_length=300)
    fecha_de_registro = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'proveedor'
        verbose_name = "Proveedor"           # Nombre singular en el admin
        verbose_name_plural = "Proveedores"


class Venta(models.Model):
    id_venta = models.AutoField(primary_key=True)
    fecha_y_hora = models.DateTimeField(blank=True, null=True)
    total = models.DecimalField(max_digits=15, decimal_places=3)
    id_cliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='id_cliente')

    class Meta:
        managed = False
        db_table = 'venta'
        verbose_name = "Venta"           # Nombre singular en el admin
        verbose_name_plural = "Ventas"
