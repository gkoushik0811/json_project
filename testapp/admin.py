from django.contrib import admin
from testapp.models import Employee
# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list_display=['id','eno','ename','eLocation','start_time','end_time']

admin.site.register(Employee,EmployeeAdmin)
