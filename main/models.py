from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
# Create your models here.


class Turial(models.Model):
    turial_title = models.CharField( max_length=200)
    turial_content = models.TextField()
    turial_publish = models.DateTimeField("date publisher", default = datetime.now())

    def __str__(self):
        return self.turial_title
    
class UserCreated(User):
    user_id = models.IntegerField(auto_created=True,primary_key=True)
    # username = models.CharField(max_length=255)
    # password = models.CharField(max_length=255, )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.username
    
class Post(models.Model):
    CATEGORY = (
			('RSA', 'RSA'),
			('ECC', 'ECC'),
            ('DSA', 'DSA'),
			) 
    file_id = models.IntegerField(auto_created=True,primary_key=True)
    title = models.CharField(max_length=255)
    decription = models.TextField()
    file = models.FileField(upload_to="up_load_file/")
    keyencrytion = models.CharField(null=True, choices=CATEGORY, max_length=255,default='RSA')
    owner = models.ForeignKey(User, related_name='post', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
        