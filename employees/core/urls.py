from django.conf.urls import url

from employees.core.api.views import EmployeeViewSet
from employees.core.views import index


app_name = 'core'
urlpatterns = [
    url(r'^employees/', EmployeeViewSet.as_view(), name='employees-api'),
    url(r'^$',index, name='index')

]
