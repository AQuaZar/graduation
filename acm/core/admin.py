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
    list_display = [
        "student",
        "datetime",
    ]
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
