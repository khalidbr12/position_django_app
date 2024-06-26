from django.contrib import admin
from .models import Product

admin.site.site_header = 'Admin Panel'
admin.site.site_title = 'Docker Socomadis Admin'
admin.site.index_title = 'Administration'

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'reference', 'position', 'active', 'category')
    search_fields = ('name', 'reference') 

# Register your models here.
admin.site.register(Product, ProductAdmin)
