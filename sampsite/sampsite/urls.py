from django.conf.urls import url
from django.contrib import admin
from sampsite.views import hello_world, root_page, random_number
from django.conf.urls import include


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^helloworld/$', hello_world),
    url(r'^$', root_page),
    url(r'^random/(\d+)/$', random_number),
    url(r'^polls/', include('polls.urls')),
]
