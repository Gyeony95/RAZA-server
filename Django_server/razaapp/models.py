from django.db import models

# Create your models here.
class Register(models.Model):
    email = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    profile_image = models.ImageField(upload_to = '', default = 'default_image.PNG')
    profile_image2 = models.ImageField(upload_to = '', default = 'default_image.PNG')
    gender = models.CharField(max_length=200)
    like = models.IntegerField(default=0)
    profile_text = models.CharField(max_length=200)

    def __str__(self):
        return self.email


class Friends(models.Model):
    subject = models.CharField(max_length=200)
    real_id = models.IntegerField(default=0)
    email = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    profile_image = models.CharField(max_length=200)
    profile_image2 = models.CharField(max_length=200)
    gender = models.CharField(max_length=200)
    like = models.IntegerField(default=0)
    profile_text = models.CharField(max_length=200)

    def __str__(self):
        return self.email

class Last_Friends(models.Model):
    real_id = models.IntegerField(default=0)
    subject = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    profile_image = models.ImageField(upload_to = '', default = 'default_image.PNG')
    profile_image2 = models.ImageField(upload_to = '', default = 'default_image.PNG')
    gender = models.CharField(max_length=200)
    profile_text = models.CharField(max_length=200)
    like_check = models.BooleanField(default= False)
    create_date = models.DateTimeField(auto_now_add= True)

    def __str__(self):
        return self.email

class Chat_List(models.Model):
    roomName = models.CharField(max_length=200)
    user_one = models.IntegerField(default=0)
    user_two = models.IntegerField(default=0)
    name = models.CharField(max_length=200)
    name2 = models.CharField(max_length=200)
    profile_image = models.CharField(max_length=200)
    script = models.CharField(max_length=200)
    date_time = models.CharField(max_length=200)
    non_read_count = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Chat_Bubble(models.Model):
    roomName = models.CharField(max_length=200)
    user_one = models.IntegerField(default=0)
    user_two = models.IntegerField(default=0)
    user_id = models.IntegerField(default=0)
    name = models.CharField(max_length=200)
    profile_image = models.CharField(max_length=200)
    script = models.CharField(max_length=200)
    date_time = models.CharField(max_length=200)
    non_read_check = models.BooleanField(default=False)

    def __str__(self):
        return self.roomName
