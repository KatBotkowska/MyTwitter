from django.urls import path

from mytwitter import views

app_name = 'mytwitter'

urlpatterns = [
    path('', views.TweetView.as_view(), name='index'),
    path('add_tweet/', views.AddTweet.as_view(), name='add_tweet'),
    path('tweet/<int:tweet_id>', views.TweetDetail.as_view(), name='tweet'),
    path('messages/', views.UserMessages.as_view(), name='messages'),
    path('message/<int:message_id>', views.MessageDetail.as_view(), name='message'),
    path('add_message/', views.AddMessage.as_view(), name='add_message'),
]
