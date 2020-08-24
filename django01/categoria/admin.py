from django.contrib import admin

from .models import Category

class CategoryAdmin(admin.ModelAdmin):
    fields = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)
