from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import User


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.CharField(max_length=50)
    group_number = models.CharField(
        max_length=3, validators=[RegexValidator(r"^\d{1,10}$")]
    )

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"


class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Attendance №{self.pk}"
