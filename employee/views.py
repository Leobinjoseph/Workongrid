from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_GET
from .models import Emp

# Create your views here.

@require_GET
def search_emp(request):
    first_name = request.GET.get('first_name')

    if not first_name:
        return JsonResponse({'error': 'Missing mandatory query parameter: first_name'}, status=400)

    users = Emp.objects.filter(first_name__startswith=first_name)

    if users.exists():
        results = [{'id': emp.id, 'first_name': emp.first_name, 'last_name': emp.last_name} for emp in users]
        return JsonResponse({'results': results})


