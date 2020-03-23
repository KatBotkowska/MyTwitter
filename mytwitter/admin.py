from django.contrib import admin

from .models import Tweet, Message

admin.site.empty_value_display = '(None)'


@admin.register(Tweet)
class TweetAdmin(admin.ModelAdmin):
    list_display = ('content', 'creation_date', 'user', 'slug')
    list_filter = ['user']


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('from_user', 'to_user', 'date', 'message_content', 'read')
    list_filter = ['from_user', 'to_user']
