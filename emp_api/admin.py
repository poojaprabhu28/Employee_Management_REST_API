from django.contrib import admin
from .models import *

class DepartmentAdmin(admin.ModelAdmin):
	list_display = ('dept_id', 'dept_name')
	list_filter = ['dept_id']
	search_fields = ['dept_id', 'dept_name']

admin.site.register(Department, DepartmentAdmin)


class EmployeeAdmin(admin.ModelAdmin):
	list_display 	= ('emp_id', 'emp_name', 'email', 'department', 'salary', 'contact_num', 'join_date')
	list_filter 	= ['department', 'join_date', 'emp_id']
	search_fields 	= ['emp_id', 'emp_name', 'department', 'salary']

admin.site.register(Employee, EmployeeAdmin)
