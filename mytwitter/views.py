from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render

from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

from mytwitter.models import Tweet, Message
from mytwitter.forms import NewTweetForm, NewMessageForm


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


class TweetView(LoginRequiredMixin, generic.ListView):
    model = Tweet
    template_name = 'mytwitter/index.html'
    context_object_name = 'tweets'

    def get_queryset(self):
        return Tweet.objects.filter(user = self.request.user)

class AddTweet(LoginRequiredMixin, generic.CreateView):
    model = Tweet
    form_class = NewTweetForm
    template_name = 'mytwitter/add_tweet.html'
    success_url = reverse_lazy('mytwitter:index')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class TweetDetail(LoginRequiredMixin, generic.DetailView):
    model = Tweet
    template_name = 'mytwitter/tweet.html'
    pk_url_kwarg = 'tweet_id'
    context_object_name = 'tweet'


class UserMessages(LoginRequiredMixin, generic.ListView):
    model = Message
    template_name = 'mytwitter/messages.html'
    context_object_name = 'messages'

    def get_queryset(self):
        return Message.objects.filter(from_user= self.request.user)

    def get_context_data(self, *, object_list=None, **kwargs):
        messages_sent = Message.objects.filter(from_user=self.request.user)
        messages_get = Message.objects.filter(to_user=self.request.user)
        ctx = {'messages_sent':messages_sent, 'messages_get': messages_get}
        return ctx

class MessageDetail(LoginRequiredMixin, generic.DetailView):
    model = Message
    template_name = 'mytwitter/message.html'
    pk_url_kwarg = 'message_id'
    context_object_name = 'message'

    def get_context_data(self, **kwargs):
        ctx = super(). get_context_data(**kwargs)
        if self.object.from_user != self.request.user:
            self.object.read = True
            self.object.save()
            self.object.refresh_from_db()
        return ctx

class AddMessage(LoginRequiredMixin, generic.CreateView):
    model = Message
    form_class = NewMessageForm
    template_name = 'mytwitter/add_message.html'
    success_url = reverse_lazy('mytwitter:messages')

    def form_valid(self, form):
        form.instance.from_user = self.request.user
        return super().form_valid(form)

    def get_initial(self):
        self.initial.update({'from_user': self.request.user})
        return super().get_initial()
