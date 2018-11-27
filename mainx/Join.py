from django.shortcuts import render
from django.utils import timezone
from .models import User
from django.shortcuts import render, get_object_or_404, get_list_or_404
from requests.exceptions import HTTPError


def join(request):
    return render(request, 'join.html',
                  {'htmltitle': 'Join MSP'})


def signup(request):
    if request.POST.get('signupfrom') == 'signupformvalue':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Registering User
        returndata = createUser(name, email, password)

        return render(request, 'join.html',
                      {'htmltitle': 'Join MSP', 'formValidationsup': returndata})

    else:
        return render(request, 'join.html',
                      {'htmltitle': 'Join MSP'})


def signin(request):
    if request.POST.get('signinfrom') == 'signinformvalue':
        email = request.POST.get('inemail')
        password = request.POST.get('inpassword')
        instance = User.objects.get(uemail=email, upass=password)

        if instance.uid:
            validations = "Login Successfull!"
        else:
            validations = "Login failed!"

        context = {
                "sinstance": instance,
                "htmltitle": 'Signin MSP',
                "formValidationin": validations
            }

        print ('sign in res for ',email,password, instance.uid)


        return render(request, 'join.html', context)

    else:
        return render(request, 'join.html', {})


def createUser(name, email, passw):

    print('creating user.. ', name, email, passw)

    now = timezone.now()
    try:
        User.objects.create(
            uname=name,
            uemail=email,
            upass=passw,
            nDate=now
        )
        return 'Registration Successfully done!'
    except Exception as e:
        return 'Registration failed! '+str(e)
