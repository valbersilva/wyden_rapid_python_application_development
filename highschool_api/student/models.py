from django.db import models

# Create your models here.

class Student(models.Model):
    # Defining gender options as a tuple of tuples
    # Make the L
    GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
    )

    name = models.CharField(max_length=20)
    age = models.IntegerField()
    gender = models.CharField(max_length=20)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.name