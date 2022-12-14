from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import ProductsViewSet

router = DefaultRouter()
router.register('products', ProductsViewSet, basename='Products')

urlpatterns = router.urls
