from django.contrib import admin
from .models import Question, Choice, Settings

# Register your models here.
admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Settings)
