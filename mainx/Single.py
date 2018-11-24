from django.shortcuts import render
from .models import Courses, SingleCourse

def play(request,cid, episode):
    # fetching data
    singlecourse = SingleCourse.objects.filter(courseid = 3)

    return render(request, 'play.html', {'episode': episode, 'htmltitle': 'Playing .. '+episode, 'singlecourse': singlecourse})