from django.contrib import admin
from .models import Puns, DiaryEntry, Thoughts

# Register your models here.

admin.site.register(Puns)
admin.site.register(DiaryEntry)
admin.site.register(Thoughts)
