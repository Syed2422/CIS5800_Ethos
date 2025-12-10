from django.contrib import admin
from .models import PayrollRecord

@admin.register(PayrollRecord)
class PayrollRecordAdmin(admin.ModelAdmin):
    list_display = ("employee", "period_start", "period_end", "gross_pay", "net_pay")
    list_filter = ("period_start", "period_end")
