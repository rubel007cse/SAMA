from django.shortcuts import render

def play(request,episode):
    return render(request, 'play.html', {'episode': episode, 'htmltitle': 'Playing .. '+episode})