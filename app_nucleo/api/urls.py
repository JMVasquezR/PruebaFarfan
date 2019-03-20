from rest_framework import routers

from app_nucleo.api.views import ClienteViewSet, ProductoViewSet, ProductoClienteViewSet, TipoDocumentoViewSet

router = routers.DefaultRouter()
router.register(r'cliente', ClienteViewSet, base_name='cliente')
router.register(r'tipo-documento', TipoDocumentoViewSet, base_name='tipo-documento')
router.register(r'producto', ProductoViewSet, base_name='producto')
router.register(r'producto-cliente', ProductoClienteViewSet, base_name='producto_cliente')

urlpatterns = router.urls
