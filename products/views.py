from rest_framework import mixins, viewsets

from .models import Products
from .serializers import ProductsSerializer


class ProductsViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    serializer_class = ProductsSerializer

    def get_queryset(self):
        queryset = Products.objects.all()
        status = self.request.query_params.get('status')
        part_number = self.request.query_params.get('part_number')
        name = self.request.query_params.get('name')
        if status:
            queryset = queryset.filter(status=status)
        if part_number:
            queryset = queryset.filter(part_number=part_number)
        if name:
            queryset = queryset.filter(name=name)
        return queryset
