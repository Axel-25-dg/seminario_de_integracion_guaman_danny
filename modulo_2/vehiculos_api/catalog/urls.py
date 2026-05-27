from django.urls import path
from rest_framework.routers import DefaultRouter
from .calculate_view import calcular_area_triangulo, promedio_ventas
from .views import MarcaViewSet, VehiculoViewSet

router = DefaultRouter()
router.register(r"marcas", MarcaViewSet, basename="marcas")
router.register(r"vehiculos", VehiculoViewSet, basename="vehiculos")

urlpatterns = [
    path('triangle/area', calcular_area_triangulo, name='calcular_area_triangulo'),
    path('ventas/promedio', promedio_ventas, name='promedio_ventas'),
]

urlpatterns += router.urls