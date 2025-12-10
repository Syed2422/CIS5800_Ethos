from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework.routers import DefaultRouter

from employees.api import EmployeeViewSet
from org.api import DepartmentViewSet
from payroll.api import PayrollRecordViewSet

router = DefaultRouter()
router.register(r"employees", EmployeeViewSet, basename="employee")
router.register(r"departments", DepartmentViewSet, basename="department")
router.register(r"payroll", PayrollRecordViewSet, basename="payroll")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("accounts.urls")),  # login/logout
    path("api/", include(router.urls)),
    path("", TemplateView.as_view(template_name="dashboard.html"), name="home"),
]
