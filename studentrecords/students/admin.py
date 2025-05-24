from django.contrib import admin
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('roll_number', 'name', 'age', 'grade')
    search_fields = ('roll_number', 'name')