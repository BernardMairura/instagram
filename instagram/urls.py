from django.urls import path,re_path
from .import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views






urlpatterns=[
    path('', views.index, name='index'),
    re_path(r'^Post/New/$', views.post, name='post'),
    re_path(r'^image/(\d+)', views.single_image, name='single_image'),
    re_path(r'^profile/', views.profile_results, name='profile_results'),
    re_path(r'^new/comment/(?P<username>[-_\w.]+)$', views.new_comment, name='newComment'),
    re_path(r'^new/status/(?P<username>[-_\w.]+)$', views.new_status, name='newStatus'),
    re_path(r'^accounts/profile/', views.profile, name ='myProfile'),
    

]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)