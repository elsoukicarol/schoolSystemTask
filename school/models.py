from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


# Create your models here.

# Creating Address table and declaring the fields as properties
class Address(models.Model):
    # Difference between textfield and charfield is that textfield has no limit
    address = models.TextField()
    city = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=10)


# Creating Student table and declaring the fields as properties
class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.CharField(max_length=3)
    # Declaring a one-to-one relationship
    address = models.OneToOneField(Address, on_delete=models.CASCADE)


# Creating Subject table and declaring the fields as properties
class Subject(models.Model):
    name = models.CharField(max_length=100)
    credits = models.CharField(max_length=2)


# Creating Enrollment table that acts as a third table for the many-to-many relationship
# between subject and student
class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    enrollmentDate = models.DateTimeField()
    # These validators help us defined the accepted values for this field in the model
    grade = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(100.0)])
