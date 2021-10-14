from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model

# Create your models here.

class Riddle(models.Model):
    title   = models.CharField(max_length=100,  verbose_name='عنوان معما')
    text    = models.TextField(verbose_name='متن معما')
    publish = models.DateTimeField(default=timezone.now, verbose_name='زمان انتشار')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'معما'
        verbose_name_plural = 'معماها'


    def __str__(self):
        return self.title


class Comment(models.Model):
    user     = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, blank=True, null=True, related_name='usernames', verbose_name='نام کاربر')
    post     = models.ForeignKey(Riddle, on_delete=models.CASCADE, related_name='comments', verbose_name='دیدگاه')
    text     = models.TextField()
    likes    = models.ManyToManyField(get_user_model(), blank=True, related_name='likes', verbose_name='پسسندیدن')
    dislikes = models.ManyToManyField(get_user_model(), blank=True, related_name='dislikes', verbose_name='نپسندیدن')
    created  = models.DateTimeField(auto_now_add=True)
    updated  = models.DateTimeField(auto_now=True)

