from django.db import models
class Student(models.Model):
    roll_number = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    grade = models.CharField(max_length=10)

    def _str_(self):
        return f"{self.roll_number} - {self.name}"