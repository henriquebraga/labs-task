from django.contrib import admin
from django.utils.timezone import now

from employees.core.models import Employee
# Register your models here.


class EmployeeModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'department', 'created_at')
    date_hierarchy = 'created_at'
    search_fields = ('name', 'email')
    list_filter = ('created_at',)
    empty_value_display = '-'
    admin.site.empty_value_display = '(None)'

    def subscribed_today(self, obj):
        return obj.created_at == now().date()


admin.site.register(Employee, EmployeeModelAdmin)