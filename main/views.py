from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Employee
from .serializes import EmployeeSerializer


@api_view(['GET', 'POST'])
def employee_list(request):
    if request.method == 'GET':
        employees = Employee.objects.all()  # Fetch all employee records from the database
        serializer = EmployeeSerializer(employees, many=True)  # Serialize multiple employee instances
        return Response(serializer.data)