from django.contrib import admin

from .models import Products


class ProductsAdmin(admin.ModelAdmin):
    exclude = ('webp_image',)


admin.site.register(Products, ProductsAdmin)
