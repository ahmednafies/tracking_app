from django.contrib import admin

from shipments.models import Company, Shipment


class ShipmentAdmin(admin.ModelAdmin):
    list_display = ('tracking_no','status', 'product', 'sender', 'receiver', 'shipping_date', 'delivery_date')
    list_filter = ('sender', 'receiver')
    ordering = ('shipping_date',)

    fieldsets = (
        (None, {'fields': ['tracking_no', 'status', 'sender', 'receiver', 'product', 'shipping_date', 'delivery_date']}),
    )

    def get_readonly_fields(self, request, obj=None):
        if obj is None:
            return ()

        return 'receiver',


admin.site.register(Company)
admin.site.register(Shipment, ShipmentAdmin)
