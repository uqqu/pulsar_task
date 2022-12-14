from rest_framework import serializers
from .models import Products


class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        exclude = ('orig_image', 'webp_image')

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['image'] = {
            'path': instance.orig_image.url[:-4],
            'formats': [instance.orig_image.url[-3:], 'webp']
        }
        return data
