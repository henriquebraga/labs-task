

from django.test import TestCase
from rest_framework.test import APIRequestFactory, CoreAPIClient

from employees.core.models import Employee
from ..tests.data import EMPLOYEE_REGISTRY

class EmployeeAPITests(TestCase):
    """Tests for Employee Read-Only API."""

    def setUp(self):
        self.obj = Employee.objects.create(**EMPLOYEE_REGISTRY)
        self.resp = self.client.get('/employees/')

    def test_get(self):
        """Must return status code 200."""

        self.assertEqual(200, self.resp.status_code)

    def test_len(self):
        """Test must have one element."""
        self.assertEqual(1, len(self.resp.data))

    def test_has_fields(self):
        """Must have the following fields: name, email and department"""
        self.assertSequenceEqual(['name', 'email', 'department'], list(self.resp.data[0].keys()))


    def test_values(self):
        """Must have the following values: Henrique Braga, h.braga.albor@gmail.com, Development"""
        self.assertSequenceEqual(['Henrique Braga', 'h.braga.albor@gmail.com', 'Development'],
                                 list(self.resp.data[0].values())
                                 )


