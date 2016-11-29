from rest_framework import routers
from rest_framework.generics import ListAPIView

from employees.core.api.serializers import EmployeeSerializer
from employees.core.models import Employee


class EmployeeViewSet(ListAPIView):
    ''' API endpoint for employees' view.'''
    queryset = Employee.objects.all().order_by('name')
    router = routers.DefaultRouter()
    serializer_class = EmployeeSerializer

    authentication_classes = []
    permission_classes = []

