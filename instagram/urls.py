from django.urls import path,re_path
from .import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views






urlpatterns=[
    path('', views.index, name='index'),
    re_path(r'^profile/',views.profile, name='profile'),
    re_path(r'^search/',views.search_results,name='search_results'),
    re_path(r'^edit/',views.edit,name='edit'),
    re_path(r'^view_profile/(?P<pk>\d+)',views.view_your_profile,name='yourprofile'),
    re_path(r'^comment/(?P<pk>\d+)',views.new_comment,name='comment'),
    re_path(r'^like/(?P<operation>.+)/(?P<pk>\d+)',views.like, name='like'),
    re_path(r'^upload_image/',views.upload,name='upload'),
    re_path(r'^like/(?P<operation>.+)/(?P<pk>\d+)',views.like, name='like'),
    

]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)