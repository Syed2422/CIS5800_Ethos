from django.db import models
from employees.models import Employee

class PayrollRecord(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="payroll_records")
    period_start = models.DateField()
    period_end = models.DateField()
    gross_pay = models.DecimalField(max_digits=10, decimal_places=2)
    net_pay = models.DecimalField(max_digits=10, decimal_places=2)
    taxes = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-period_end"]

    def __str__(self):
        return f"{self.employee} - {self.period_start} to {self.period_end}"
