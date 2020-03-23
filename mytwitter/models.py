from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify


class Tweet(models.Model):
    content = models.CharField(max_length=256)
    creation_date = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=256, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.content)
            super(Tweet, self).save(*args, **kwargs)

    def __str__(self):
        return f'Tweet to {self.user} from {self.creation_date}'

    class Meta:
        ordering = ('creation_date',)


class Message(models.Model):
    message_content = models.CharField(max_length=256)
    from_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='from_user')
    to_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='to_user')
    date = models.DateField(auto_now_add=True)
    read = models.BooleanField(default=False)

    class Meta:
        ordering = ('date',)

    def __str__(self):
        return f'Tweet to {self.to_user} from {self.date}'
