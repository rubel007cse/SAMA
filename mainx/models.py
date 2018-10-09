from django.db import models

# Create your models here.

class Courses(models.Model):
    coursename = models.CharField(max_length=50, default='0')
    description = models.CharField(max_length=100, default='0')
    skills = models.CharField(max_length=50, default='0')
    thumbnailimage = models.CharField(max_length=50, default='0')
    nDate = models.DateTimeField()

    def __str__(self):
        return self.coursename

