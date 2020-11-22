from django.urls import path,re_path
from .import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views






urlpatterns=[
    path('',views.index,name='index'),
    re_path(r'^Post/New/$', views.post, name='post'),
    re_path(r'^image/(\d+)', views.single_image, name='single_image'),
    re_path(r'^profile/', views.profile_results, name='profile_results'),
    # path('search/', views.search_results, name='search_results'),
    # re_path(r'^archives/(\d{4}-\d{2}-\d{2})/$',views.past_days_news,name = 'pastNews'),
    # re_path(r'^new/article$', views.new_article, name='new-article'),
    # re_path(r'article/(\d+)', views.article, name='article'),

]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)