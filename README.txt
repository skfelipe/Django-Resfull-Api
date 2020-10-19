
ACTIVAR ENTORNO VIRUTAL.

\dj_api\djapi\entvirt\Scripts\activate.bat

DESACTIVAR ENTORNO VIRUTAL.

\dj_api\djapi\entvirt\Scripts\deactivate.bat



    #Entramos en el shell de Django
    manage.py shell

    from api.serializers import ProductoSerializer
    from api.models import Producto


    prod_serializer = ProductoSerializer(data={"subcategoria":1,"descripcion":"Desarrollo Web con Python usando Django 2.1","fecha_creado":"2018-10-01T12:11:37.090335Z"})
    prod_serializer.is_valid()
    prod1 = prod_serializer.save()
    prod1.pk

    prod_serializer = ProductoSerializer(instance=prod1, data={"subcategoria":1,"descripcion":"Desarrollo Web con Python usando Django","fecha_creado":"2018-10-01T12:11:37.090335Z"})
    prod_serializer.is_valid()
    prod_serializer.save()


Ahora veamos cómo devolver registros

    prod1 = Producto.objects.all().first()
    prod_serializer1 = ProductoSerializer(prod1)
    prod_serializer1.data

    prod2 = ProductoSerializer(Producto.objects.all(),many=True)
    prod2.data

ProductoSerializer(Producto.objects.all().first(),many=False).data