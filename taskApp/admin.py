from django.contrib import admin
from .models import *
# Register your models here.

class AdminUser(admin.ModelAdmin):
    list_display = ['first_name']
admin.site.register(User,AdminUser)  
class AdminTask(admin.ModelAdmin):
    list_display = ['task_name','created_by','status']
admin.site.register(Task,AdminTask)
class AdminEmployee(admin.ModelAdmin):
    list_display = ['user']
admin.site.register(Employee,AdminEmployee)