from django.contrib import admin
from .models import Riddle, Comment

class RiddleAdmin(admin.ModelAdmin):
    list_display = ('__str__','text', "jpublish")

# Register your models here.
admin.site.register(Riddle, RiddleAdmin)
admin.site.register(Comment)