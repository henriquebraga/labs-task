from rest_framework.serializers import ModelSerializer
from employees.core.models import Employee

class EmployeeSerializer(ModelSerializer):

    class Meta:
        model = Employee
        fields = ['name', 'email', 'department',]


