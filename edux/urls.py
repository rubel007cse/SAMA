from django.conf.urls import url, include
import mainx.views as xviews
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    url(r'^$', xviews.landingpage, name='index'),
    url('main/', include('mainx.urls')),
]

urlpatterns += staticfiles_urlpatterns()