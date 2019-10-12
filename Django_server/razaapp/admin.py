from django.contrib import admin

# Register your models here.
from razaapp.models import Register, Friends, Last_Friends, Chat_List, Chat_Bubble

admin.site.register(Register)
admin.site.register(Friends)
admin.site.register(Last_Friends)
admin.site.register(Chat_List)
admin.site.register(Chat_Bubble)
