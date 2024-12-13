from django.contrib import admin

from .models import Employee,franchisesales

# Register your models here.


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = (
        "employee_id",
        "username",
        "email",
        "password",
        "employee_type",
        'phone_number'
    )

admin.site.register(franchisesales)