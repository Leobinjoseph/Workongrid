from django.urls import path
from employee.views import search_emp

urlpatterns = [
    path('api/users/', search_emp, name='search_emp'),
]
