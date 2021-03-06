from django.conf.urls import url
from . import Users, Courses, Single, Join

urlpatterns = [
    url(r'^profile', Users.profile, name="profile"),
    url(r'^courses', Courses.courses, name="courses"),
    url(r'^course/(?P<id>.+)/(?P<cname>.+)/$', Courses.singlecourse, name="single"),
    url(r'^join', Join.join, name="join"),
    url(r'^signup', Join.signup, name="signup"),
    url(r'^signin', Join.signin, name="signin"),
    url(r'^myprofile', Users.profile, name="myprofile"),
]
