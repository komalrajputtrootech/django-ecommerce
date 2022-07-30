from django.contrib import admin

from product.models import Product, Category

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug",)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product)
