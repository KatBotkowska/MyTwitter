from django.urls import path

from mytwitter import views


urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
]