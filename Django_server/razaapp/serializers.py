from rest_framework import serializers

from razaapp.models import Register, Friends, Last_Friends, Chat_List, Chat_Bubble


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Register
        fields = ('id','name','email','country', 'password', 'profile_image', 'profile_image2', 'gender', 'profile_text' , 'like')

class FriendsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Friends
        fields = ('id','subject','real_id','name','email','country',  'profile_image', 'profile_image2', 'gender', 'profile_text' , 'like')


class Last_FriendsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Last_Friends
        fields = ('id','real_id','subject','name','email','country',  'profile_image', 'profile_image2', 'gender', 'profile_text' , 'like_check', 'create_date')


class Chat_ListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat_List
        fields = ('id','roomName','user_one','user_two','name','name2','profile_image','script','date_time','non_read_count')

class Chat_BubbleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat_Bubble
        fields = ('id','roomName','user_one','user_two','user_id','name','profile_image','script','date_time','non_read_check')
