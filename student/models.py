from django.db import models
from django.contrib.auth.models import User
from django_extensions.db.models import TimeStampedModel
from django.utils import timezone


# Create your models here.

class School(TimeStampedModel):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    principal_name = models.CharField(max_length=100)

    def __str__(self):
        return "%s - %s" % (self.name, self.phone_number)

class Class(TimeStampedModel):
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    teacher_name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return "%s - %s" % (self.name, self.teacher_name)

class Student(TimeStampedModel):
    class_field = models.ForeignKey(Class, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    address = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return "%s - %s" % (self.first_name, self.last_name)

class Teacher(TimeStampedModel):
    id = models.IntegerField(primary_key=True)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    qualification = models.CharField(max_length=100)

    def __str__(self):
        return "%s - %s" % (self.name, self.qualification)

class Subject(TimeStampedModel):
    name = models.CharField(max_length=100)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    class_field = models.ForeignKey(Class, on_delete=models.CASCADE)

    def __str__(self):
        return "%s - %s" % (self.name, self.teacher)

class Attendance(TimeStampedModel):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateField()
    is_present = models.BooleanField(default=False)

    def __str__(self):
        return "%s - %s" % (self.date, self.is_present)

class Exam(TimeStampedModel):
    class_field = models.ForeignKey(Class, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    date = models.DateField()
    maximum_marks = models.PositiveIntegerField()

    def __str__(self):
        return "%s - %s" % (self.subject, self.maximum_marks)

class ExamResult(TimeStampedModel):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    obtained_marks = models.PositiveIntegerField()

    def __str__(self):
        return "%s - %s" % (self.student, self.obtained_marks)




    