from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions, status , generics, filters
from rest_framework.permissions import *
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.schemas import AutoSchema

from .models import *
from .serializers import *
import coreapi


class DeptDetail(AutoSchema):
    """return department details"""
	def get_dept_data(self, path, method):
		dept_data_db = []
		if method.lower() in ['post', 'put']:
			dept_data_db = [
				coreapi.Field('dept_name')
			]
		dept_data = super().get_manual_fields(path, method)
		return dept_data + dept_data_db


class EmpDetail(AutoSchema):
    """Return Employee details"""
	def get_emp_data(self, path, method):
		emp_data_db	= []
		if method.lower() in ['post', 'put']:
			emp_data_db	= [
				coreapi.Field('emp_name'),
				coreapi.Field('email'),
				coreapi.Field('contact_num'),
				coreapi.Field('salary'),
				coreapi.Field('department'),
			]
		emp_data = super().get_manual_fields(path, method)
		return emp_data + emp_data_db

class DeptDetail(APIView):
    """Display Departmentdetails"""
	serializer_class = DepartmentSerializer
	schema = DptViewSchema()

	def get(self, request, slug):
		dpt_det	= get_object_or_404(Department.objects.all(), code=slug)
		serializer = DepartmentSerializer(dpt_det, many=False)
		return Response({"dpt_details": serializer.data})

class EmpAdd(APIView):
    """Create employee"""
	serializer_class = EmployeeSerializer
	schema = EmpViewSchema()

	def get(self, request):
		emp_det	= Employee.objects.all()
		serializer = EmployeeDisplaySerializer(emp_det, many=True)
		return Response({"emp_details": serializer.data})

	def post(self, request):
		emp_det = request.data
		serializer = EmployeeSerializer(data=emp_det)
		if serializer.is_valid(raise_exception=True):
			emp_det_saved = serializer.save()
			return Response({"success": "Employee is '{}' created successfully".format(emp_det_saved.name)}, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EmpView(APIView):
    """Update Employee details"""
	serializer_class = EmployeeSerializer
	schema = EmpViewSchema()
	def get(self, request, pk):
		emp_details	= get_object_or_404(Employee.objects.all(), pk=pk)
		serializer = EmployeeSerializer(emp_details, many=False)
		return Response({"emp_details": serializer.data})

	def put(self, request, pk):
		saved_emp_det = get_object_or_404(Employee.objects.all(), pk=pk)
		data = request.data
		serializer = EmployeeSerializer(instance=saved_emp_det, data=data, partial=True)
		if serializer.is_valid(raise_exception=True):
			emp_det_saved = serializer.save()
		return Response({"success": "Employee '{}' updated successfully".format(emp_det_saved.name)})

class EmpSearchView(APIView):
    """Displays employee details based on salary"""
	serializer_class = EmployeeSerializer
	# schema 					= SearchSchema()
	def get(self, request):
		emp_det	= Employee.objects.all()
		print(request.data)

		try:
			max_salary
			emp_det	= emp_det.filter(salary__lte=max_salary)
		except:
			pass

		try:
			min_salary = request.data.get('minumum_salary')
			emp_det = emp_det.filter(salary__gte=min_salary)
		except:
			pass

		serializer = EmployeeDisplaySerializer(emp_det, many=True)
