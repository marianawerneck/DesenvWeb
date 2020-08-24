from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    fields = ('category', 'name', 'slug', 'branch', 'quantity', 'price', 'available', 'image')
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Product, ProductAdmin)