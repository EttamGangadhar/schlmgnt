#from django.db import models
#from django.contrib.auth.models import User
#from django_extensions.db.models import TimeStampedModel
#from student.models import Teacher


# Create your models here.
#class CourseInfo(TimeStampedModel):
    #course_name =models.CharField(max_length=100)
    #course_desc =models.CharField(max_length=100000)
    #teacher_id = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    #is_active = models.BooleanField(default=True)


#class ClassInfo(TimeStampedModel):
 #   class_name =models.CharField(max_length=50)
  #  teacher_id = models.ForeignKey(Teacher, on_delete=models.CASCADE)
   # is_active = models.BooleanField(default=True)

#class Subjects(TimeStampedModel):
 #   sub_name = models.CharField(max_length=50)
  #  is_active = models.BooleanField(default=True)

#class TimeTable(TimeStampedModel):
 #   cls_id = models.ForeignKey(ClassInfo, on_delete=models.CASCADE)
  #  sub_id = models.ForeignKey(Subjects, on_delete=models.CASCADE)
   # day_choices = (
    #    ('MON', 'Monday'),
     #  ('WED', 'Wednesday'),
      # ('FRI', 'Friday'),
       # ('SAT', 'Saturday'),
       # ('SUN', 'Sunday'),
    #)
    #day_of_week = models.CharField(choices=day_choices, max_length=20)
    #start_time = models.TimeField(auto_now_add=True)
    #end_time = models.TimeField(auto_now_add=True)
    