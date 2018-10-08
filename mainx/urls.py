from django.conf.urls import url
from . import Users, Courses, Single


urlpatterns = [
    url(r'^profile', Users.profile, name="profile"),
    url(r'^courses', Courses.courses, name="courses"),
    url(r'^play/(?P<episode>.+)/$', Single.play, name="play"),
]