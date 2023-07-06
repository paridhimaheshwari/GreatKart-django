from django.contrib import admin
from . models import Product, Variation

class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'price', 'stock', 'category', 'modified_date', 'is_available')
    prepopulated_fields = {'slug': ('product_name',)}

class VariationAdmin(admin.ModelAdmin):
    list_display = ('product', 'get_related', 'variation_category', 'variation_value', 'is_active')
    list_editable = ('is_active',)
    list_filter = ('product__product_name', 'variation_category', 'variation_value')

    def get_related(self, obj):
            """
            Get some related data
            """
            return obj.product.product_name
    get_related.short_description = 'Product Name'
admin.site.register(Product, ProductAdmin) 
admin.site.register(Variation, VariationAdmin)