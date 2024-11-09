from django.contrib import admin
from .models import Order, OrderItem, OrderItemWD, OrderWithoutDelivery


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'phone_number',
                    'address', 'paid',
                    'created', 'updated']
    list_filter = ['created']
    inlines = [OrderItemInline]


admin.site.register(Order, OrderAdmin)


class OrderWdItemInline(admin.TabularInline):
    model = OrderItemWD
    raw_id_fields = ['product']


class OrderWDAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'phone_number']
    list_filter = ['created']
    inlines = [OrderWdItemInline]


admin.site.register(OrderWithoutDelivery, OrderWDAdmin)

admin.site.register(OrderItemWD)
admin.site.register(OrderItem)