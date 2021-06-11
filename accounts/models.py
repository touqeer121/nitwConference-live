from django.db import models
from django.contrib.auth.models import User
from conference.models import *
from django.core.files.storage import FileSystemStorage
from django.conf import settings
import datetime
from gdstorage.storage import GoogleDriveStorage
gd_storage = GoogleDriveStorage()

class TrackChairProfile(models.Model):
    user = models.OneToOneField(User,related_name='profile', on_delete=models.CASCADE)
    phone = models.CharField(max_length=20,null=True, blank=True)
    track = models.CharField(max_length=255,null=True)
    institution = models.CharField(max_length=255,null=True, blank=True)
    profile_pic = models.ImageField(upload_to='maps' ,null=True, blank=True)
    prefix = models.CharField(max_length=255, blank=True)
    
    def __str__(self):
        return self.user.username
