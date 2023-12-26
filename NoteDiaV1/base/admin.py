from django.contrib import admin
from .models import Room,Topic,Message,User,UserTopic



class TopicInline(admin.TabularInline):
    model = UserTopic
    extra = 1

class UserAdmin(admin.ModelAdmin):
    inlines = (TopicInline,)

admin.site.register(User, UserAdmin)
admin.site.register(Topic)
admin.site.register(Room)
admin.site.register(Message)
