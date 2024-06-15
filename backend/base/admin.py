from django.contrib import admin
from.models import Product, Review, Order, OrderItem, ShippingAddress

class ProductsAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand', 'category', 'price', 'rating', 'numReviews', 'countInStock', 'createdAt')
    list_filter = ('category', 'rating')
    search_fields = ['name', 'brand']
    ordering = ['-createdAt']

class ProductReviewAdmin(admin.ModelAdmin):
    list_display = ('product', 'user', 'name', 'rating', 'comment', '_id')
    list_filter = ('product', 'rating')
    search_fields = ['name', 'comment']

class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'paymentMethod', 'taxPrice', 'shippingPrice', 'totalPrice', 'isPaid', 'paidAt', 'isDelivered', 'deliveredAt', 'createdAt')
    list_filter = ('isPaid', 'isDelivered')
    search_fields = ['user__username']  

class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('product', 'order', 'name', 'qty', 'price', 'image', '_id')
    list_filter = ('order',)
    search_fields = ['product__name', 'order__user__username'] 

class ShippingAddressAdmin(admin.ModelAdmin):
    list_display = ('order', 'country', 'city', 'address', 'postalCode', 'shippingPrice', '_id')
    list_filter = ('order',)
    search_fields = ['order__user__username', 'address'] 

# Register your models with the custom ModelAdmins
admin.site.register(Product, ProductsAdmin)
admin.site.register(Review, ProductReviewAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
admin.site.register(ShippingAddress, ShippingAddressAdmin)
