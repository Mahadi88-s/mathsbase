from django.contrib import admin
from .models import QuestionP2, QuestionP1, QuestionP3, Profile, Pwdlist

# Register your models here.
admin.site.register(QuestionP1)
admin.site.register(QuestionP2)
admin.site.register(QuestionP3)
admin.site.register(Profile)
admin.site.register(Pwdlist)