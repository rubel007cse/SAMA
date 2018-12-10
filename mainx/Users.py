from django.shortcuts import render
from .models import User


def profile(request):
    if request.session.has_key('userid'):
        uid = request.session['userid']
        instance = User.objects.get(uid=uid)
        return render(request, 'profile.html', {'htmltitle': 'My Profile',
                                                'uname': instance.uname, 'isactive_profile' : 'active'})
    else:
        return render(request, 'join.html', {'htmltitle': 'Join Us', 'isactive_profile' : 'active'})
