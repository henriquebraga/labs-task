from django.test import TestCase
from employees.core.models import Employee
from datetime import datetime

from employees.core.tests.data import EMPLOYEE_REGISTRY


class EmployeeModelTest(TestCase):

    def setUp(self):
        self.obj = Employee.objects.create(**EMPLOYEE_REGISTRY)

    def test_create(self):
        self.assertTrue(Employee.objects.exists())

    def test_created_at(self):
        """Employee must have an auto created at attr."""
        self.assertIsInstance(self.obj.created_at, datetime)

    def test_str(self):
        self.assertEqual('Henrique Braga', str(self.obj))
