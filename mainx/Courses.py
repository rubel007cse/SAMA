from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.utils import timezone
from .models import Courses,SingleCourse


def courses(request):

    # fetching data
    instance = get_list_or_404(Courses)

    context = {
        "courselist": instance,
        'htmltitle': 'Courses',
        'isactive_courses' : 'active'
    }
    return render(request,
                  'courses.html', context)



def singlecourse(request, id=None, cname=None):

    # fetching data
    instance = get_list_or_404(SingleCourse, courseid_id=id)
    context = {
        "sinstance": instance,
        'htmltitle': 'Single Course',
        'isactive': 'active'
    }

    return render(request,
                  'singlecourse.html', context)









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
