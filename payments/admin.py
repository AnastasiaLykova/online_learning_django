from django.contrib import admin

from payments.models import Payments


@admin.register(Payments)
class PaymentsAdmin(admin.ModelAdmin):
    list_display = ('user', 'datetime', 'course','lesson', 'payment_amount', 'payment_method')
    list_filter = ('user',)
    search_fields = ('user',)
