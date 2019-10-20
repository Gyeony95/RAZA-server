from django.conf.urls import url
from django.urls import path, include
from . import views #.은 현재폴더의 디렉토리라는뜻. 즉 현재폴더의 views.py를 import하는것임

app_name = 'razaapp'
urlpatterns = [
path('',  include('rest_framework.urls', namespace='rest_framework_category')),
url(r'^upload/$', views.RegisterAPIView.as_view()),
url(r'^upload/$', views.FriendsAPIView.as_view()),
url(r'^upload/$', views.Last_FriendsAPIView.as_view()),
url(r'^upload/$', views.Chat_ListAPIView.as_view()),
url(r'^upload/$', views.Chat_BubbleAPIView.as_view()),
]