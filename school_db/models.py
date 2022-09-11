from django.db import models

class Student(models.Model):
    # This defines and connects to the "first_name" column in the students table
    # The data type of this column will be a varchar with a max length of 40 characters
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    # Integer data type column (whole number)
    year = models.IntegerField(default=9)
    # Float data type column (decimal number)
    gpa = models.FloatField()



# Create your models here.

class Instructor(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    hire_date = models.DateField()



class Course(models.Model):
    name = models.CharField(max_length=40)
    instructor = models.ForeignKey(Instructor, null=True, blank=True, on_delete=models.SET_NULL)
    credits = models.IntegerField()

class StudentCourse(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    grade = models.CharField(max_length=20)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['student', 'course'], name='unique_student_course')
        ]
