from django.contrib import admin
from .models import Employee,Department,Designation,Unitname,Office
# Register your models here.
admin.site.register(Employee)
admin.site.register(Department)
admin.site.register(Designation)
admin.site.register(Unitname)
admin.site.register(Office)
