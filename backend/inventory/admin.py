from django.contrib import admin
from .models import (Category, SubCategory, Product,)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    list_display_links = ('id', 'name',)
    search_fields = ('name',)
    list_per_page = 25

admin.site.register(Category, CategoryAdmin)

class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'name',)
    list_display_links = ('id', 'name',)
    search_fields = ('name',)
    list_per_page = 25

admin.site.register(SubCategory, SubCategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'subcategory', 'name',)
    list_display_links = ('id', 'name',)
    search_fields = ('name',)
    list_per_page = 25

admin.site.register(Product, ProductAdmin)
