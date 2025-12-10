from rest_framework import serializers
from .models import PayrollRecord

class PayrollRecordSerializer(serializers.ModelSerializer):
    employee_name = serializers.CharField(source="employee.__str__", read_only=True)

    class Meta:
        model = PayrollRecord
        fields = "__all__"
