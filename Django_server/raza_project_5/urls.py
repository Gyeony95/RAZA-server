"""raza_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import routers
from django.conf import settings
from razaapp import views
from django.conf.urls.static import static


router = routers.DefaultRouter()
router.register(r'registers', views.RegisterViewSet)
router.register(r'friends', views.FriendsViewSet)
router.register(r'last_friends', views.Last_FriendsViewSet)
router.register(r'chat_lists', views.Chat_ListViewSet)
router.register(r'chat_bubbles', views.Chat_BubbleViewSet)



urlpatterns = [
    path('razaapp/', include('razaapp.urls')),
    path('', include(router.urls)),
    re_path('admin/', admin.site.urls),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


