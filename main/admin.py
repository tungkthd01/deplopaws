from django.contrib import admin
from .models import Turial,Post,UserCreated
from django.db import models
from tinymce.widgets import TinyMCE
# Register your models here.
class TutorialAdmin(admin.ModelAdmin):
    # fields = ["turial_title",
    #             "turial_publish",
    #             "turial_content"]
    fieldsets = [
        ("Title/date",{"fields":["turial_title","turial_publish"]}),
        ("Content",{"fields":["turial_content"]})
    ]
   
class PostAdmin(admin.ModelAdmin):
    fields = ["file_id","title","decription","file","keyencrytion","owner"]
    
class UserCreatedAdmin(admin.ModelAdmin):
    fields = ["user_id","username","email","password"]
       
admin.site.register(Turial, TutorialAdmin)
admin.site.register(Post , PostAdmin)
