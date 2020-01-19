from django.conf.urls import url
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls import static
from django.conf.urls.static import static

urlpatterns=[
    url(r'^$',views.home,name='home'),
    url(r'^onehood/(\d+)',views.one_hood,name='onehood'),
    url(r'^newpost/$',views.post,name='post'),
    url(r'^business/$',views.business,name='business'),
    url(r'^join_hood/(\d+)',views.join_hood,name='join-hood'),
    url(r'^leave_hood/(\d+)',views.leave_hood,name='leave-hood'),
    path('profile/',views.profile,name = 'profile'),
    url(r'^newhood/$',views.new_hood,name='newhood'),
    url(r'^search/',views.search_results,name = 'search_results'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)