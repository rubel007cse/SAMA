from django.shortcuts import render

def join(request):

    return render(request, 'join.html', {'htmltitle': 'Join MSP'})



def signup(request):

    return render(request, 'join.html', {'htmltitle': 'Join MSP'})


def signin(request):

    return render(request, 'join.html', {'htmltitle': 'Join MSP'})
