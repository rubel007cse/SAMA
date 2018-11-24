from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.utils import timezone
from .models import Courses,SingleCourse


def courses(request):

    # fetching data
    instance = get_list_or_404(Courses)

    print('it', instance)
    context = {
        "courselist": instance,
        'htmltitle': 'Courses'
    }
    return render(request,
                  'courses.html', context)



def singlecourse(request, id=None, cname=None):

    # fetching data
    instance = get_object_or_404(SingleCourse, id =id)
    context = {
        "sctitle": instance.episodetitle,
        "sinstance": instance,
        'htmltitle': 'Single Course'
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
