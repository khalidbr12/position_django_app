from django.contrib import admin
from .models import Product

admin.site.site_header = 'Admin Pannel'
admin.site.site_title = 'Docker Socomadis Admin'
admin.site.index_title = 'Administration'

# Register your models here.
admin.site.register(Product)
