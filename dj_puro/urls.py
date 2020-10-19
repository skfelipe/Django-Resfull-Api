from django.urls import path
from .views import categoria_destalle, categoria_list

urlpatterns = [
    path('categorias/', categoria_list, name="categoria_list"),
    path('categorias/<int:pk>', categoria_destalle, name="categoria_detalle"),
]