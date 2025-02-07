from django.urls import path
from . import views

app_name = 'tiendamusical'

urlpatterns = [
    path("", views.index, name="index"),
] 