from rest_framework import viewsets, permissions
from .models import PayrollRecord
from .serializers import PayrollRecordSerializer

class PayrollRecordViewSet(viewsets.ModelViewSet):
    queryset = PayrollRecord.objects.select_related("employee").all()
    serializer_class = PayrollRecordSerializer
    permission_classes = [permissions.IsAuthenticated]
