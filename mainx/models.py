from django.db import models

# Create your models here.

class Courses(models.Model):
    coursename = models.CharField(max_length=50, default='0')
    description = models.CharField(max_length=100, default='0')
    skills = models.CharField(max_length=50, default='0')
    thumbnailimage = models.CharField(max_length=50, default='0')
    nDate = models.DateTimeField()

class SingleCourse(models.Model):
    courseid = models.ForeignKey(Courses, on_delete=models.CASCADE)
    episodetitle = models.CharField(max_length=100, default='0')
    episodedesc = models.CharField(max_length=50, default='0')
    episodethumbnailimage = models.CharField(max_length=50, default='0')
    episodeURL = models.CharField(max_length=50, default='0')
    nDate = models.DateTimeField()



class User(models.Model):
    uid = models.CharField(primary_key=True,max_length=20)
    uname = models.CharField(max_length=20, default='0')
    uemail = models.CharField(max_length=30, default='0')
    upass = models.CharField(max_length=20, default='0')
    uImg = models.CharField(max_length=50, default='0')
    nDate = models.DateTimeField()