from django.forms import ModelForm, Textarea
from .models import Tweet, Message, User


class NewTweetForm(ModelForm):
    class Meta:
        model = Tweet
        fields = ('content',)
        widgets = {
            'content': Textarea(attrs={'cols': 80, 'rows': 5}),
        }


class NewMessageForm(ModelForm):
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('initial')['from_user']
        super().__init__(*args, **kwargs)
        self.fields['to_user'].queryset = User.objects.exclude(id=user.id)

    class Meta:
        model = Message
        fields = ('to_user', 'message_content',)
        widgets = {
            'message_content': Textarea(attrs={'cols': 80, 'rows': 5}),
        }
