from django.shortcuts import render
from django.utils import timezone
from .models import Courses


def courses(request):

    # fetching data
    allcourses = [c for c in Courses.objects.all()]

    return render(request, 'courses.html', {'htmltitle': 'Courses', 'courselist': allcourses})


def createCourse(name, desc, skills, imagelink):
    now = timezone.now()
    try:
        Courses.objects.create(
            coursename=name,
            description=desc,
            skills=skills,
            thumbnailimage=imagelink,
            nDate=now
        )
        return 'success'
    except:
        return 'fail'
