from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import Student, Attendance

# Define an inline admin descriptor for Student model


class StudentsInline(admin.StackedInline):
    model = Student
    can_delete = False
    verbose_name_plural = "students"


# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (StudentsInline,)


# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)


@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ["student", "datetime", "get_department", "get_group_number"]
    list_filter = [
        "student",
        "datetime",
    ]
    search_fields = [
        "student__user__first_name",
        "student__user__last_name",
        "datetime__day",
        "datetime__month",
        "datetime__year",
    ]

    def get_department(self, obj):
        return obj.student.department

    get_department.admin_order_field = "student"  # Allows column order sorting
    get_department.short_description = "Department"  # Renames column head

    def get_group_number(self, obj):
        return obj.student.group_number

    get_group_number.admin_order_field = "student"
    get_group_number.short_description = "Group Number"
