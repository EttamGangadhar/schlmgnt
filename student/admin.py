from django.contrib import admin
from student.models import *
# Register your models here.

admin.site.register((School, Class, Student, Teacher,Subject, Attendance, Exam, ExamResult))
