from django.db import models
from django.utils import timezone

# Create your models here.
class Riddles(models.Model):
    title = models.CharField(max_length=100,  verbose_name='عنوان معما')
    text = models.TextField(verbose_name='متن معما')
    publish = models.DateTimeField(default=timezone.now, verbose_name='زمان انتشار')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'معما'
        verbose_name_plural = 'معماها'


    def __str__(self):
        return self.title