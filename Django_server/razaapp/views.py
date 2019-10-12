from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.generics import CreateAPIView

from razaapp.models import Register, Friends, Last_Friends, Chat_List, Chat_Bubble
from razaapp.serializers import RegisterSerializer, FriendsSerializer, Last_FriendsSerializer, Chat_ListSerializer, \
    Chat_BubbleSerializer


class RegisterViewSet(viewsets.ModelViewSet):
    queryset = Register.objects.all()
    serializer_class = RegisterSerializer

class FriendsViewSet(viewsets.ModelViewSet):
    queryset = Friends.objects.all()
    serializer_class = FriendsSerializer



class Last_FriendsViewSet(viewsets.ModelViewSet):
    queryset = Last_Friends.objects.all()
    serializer_class = Last_FriendsSerializer

class Chat_ListViewSet(viewsets.ModelViewSet):
    queryset = Chat_List.objects.all()
    serializer_class = Chat_ListSerializer


class Chat_BubbleViewSet(viewsets.ModelViewSet):
    queryset = Chat_Bubble.objects.all()
    serializer_class = Chat_BubbleSerializer





class RegisterAPIView(CreateAPIView):
	serializer_class = RegisterSerializer
	queryset = Register.objects.all()

class FriendsAPIView(CreateAPIView):
	serializer_class = FriendsSerializer
	queryset = Friends.objects.all()

class Last_FriendsAPIView(CreateAPIView):
	serializer_class =Last_FriendsSerializer
	queryset = Last_Friends.objects.all()

class Chat_ListAPIView(CreateAPIView):
	serializer_class =Chat_ListSerializer
	queryset = Chat_List.objects.all()

class Chat_BubbleAPIView(CreateAPIView):
	serializer_class =Chat_BubbleSerializer
	queryset = Chat_Bubble.objects.all()
