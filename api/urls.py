from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views

from rest_framework.documentation import include_docs_urls

from api.apiviews import ProductoList, ProductoDetalle, CategoriaSave, SubCategoriaSave, CategoriaList, SubCategoriaList, \
    CategoriaDetalle, SubCategoriasAdd, ProductoViewSet, UserCreate, LoginView

router = DefaultRouter()
router.register('v2/productos', ProductoViewSet, basename="productos")

urlpatterns = [
    path('v1/productos/', ProductoList.as_view(), name='producto_list'),
    path('v1/productos/<int:pk>', ProductoDetalle.as_view(), name='producto_detalle'),
    path('v1/categorias/', CategoriaList.as_view(), name='categoria_save'),
    #path('v1/subcategorias/', SubCategoriaList.as_view(), name='subcategoria_save'),
    path('v1/categorias/save/', CategoriaSave.as_view(), name='categoriasave'),
    path('v1/subcategorias/save/', SubCategoriaSave.as_view(), name='subcategoriasave'),
    path('v1/categorias/<int:pk>', CategoriaDetalle.as_view(), name='categoria_detalle'),
    path('v1/categorias/<int:pk>/subcategorias/', SubCategoriaList.as_view(), name='sc_list'),
    path('v1/categorias/<int:cat_pk>/addsubcategorias/', SubCategoriasAdd.as_view(), name='sc_add'),
    path('v3/usuarios/', UserCreate.as_view(), name='usuario_crear' ),
    path("v4/login/", LoginView.as_view(), name="login"),
    path('v4/login-drf/', views.obtain_auth_token, name="login_drf"),
    path('coreapi-docs/', include_docs_urls(title='Documentacion COREAPI')),

]

urlpatterns += router.urls