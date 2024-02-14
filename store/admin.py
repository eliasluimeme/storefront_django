from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price']
    list_editable = ['price']
    list_per_page = 10
    search_fields = ['title']

admin.site.register(models.Collection)
# admin.site.register(models.Product)
admin.site.register(models.Promotion)