# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.files.storage import FileSystemStorage


from django.db.models.signals import pre_save
from django.dispatch import receiver
import os

class uploadfolder(models.Model):
    """ my application """
    File_to_upload = models.FileField(upload_to='')
#add this two functions if you want to pre delete/overwrite existing file when uploading up
#signals
@receiver(pre_save, sender=uploadfolder)
def file_update(sender, **kwargs):
    upload_folder_instance = kwargs['instance']
    if upload_folder_instance.File_to_upload:
        path = upload_folder_instance.File_to_upload.path
        os.remove(path)
#end signals



class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    #employee_code=models.CharField(max_length=100,default='')
    sex=(
            ('Male','Male'),
            ('Female','Female'),

    )

    Gender=models.CharField(max_length=100,choices=sex,blank=True,default='')
    Phone=models.CharField(max_length=20,blank=True,default='')
    island=models.CharField(max_length=100,blank=True,default='')
    city=models.CharField(max_length=100,blank=True,default='')
    country=models.CharField(max_length=100,blank=True,default='')
    organization=models.CharField(max_length=100,blank=True,default='')


    def __unicode__(self):
        return self.user.first_name


def create_profile(sender, **kwargs):
    user = kwargs["instance"]
    if kwargs["created"]:
        user_profile = Profile(user=user)
        user_profile.save()
post_save.connect(create_profile, sender=User)



class contacts(models.Model):
    First_Name = models.CharField(max_length = 60,default='')
    Middle_Name = models.CharField(max_length = 60,default='',null=True)
    Last_Name = models.CharField(max_length = 60,default='')
    Date_of_Birth=models.DateField(null=True,blank=True)
    sex=(('Male','Male'),
        ('Female','Female'),

        )

    Gender=models.CharField(max_length=100, choices=sex,blank=True,default='')

    isl=(('Torres','Torres'),
        ('Banks','Banks'),
        ('Santo','Santo'),
        ('Ambae','Ambae'),
        ('Pentecost','Pentecost'),
        ('Maewo','Maewo'),
        ('Malekula','Malekula'),
        ('Ambrym','Ambrym'),
        ('Paama','Paama'),
        ('Epi','Epi'),
        ('Tongoa','Tongoa'),
        ('Tongariki','Tongariki'),
        ('Emae','Emae'),
        ('Makira','Makira'),
        ('Mataso','Mataso'),
        ('Efate','Efate'),
        ('Erromango','Erromango'),
        ('Tana','Tana'),
        ('Aniwa','Aniwa'),
        ('Futuna','Futuna'),

        )

    Island=models.CharField(max_length=100, choices=isl,blank=True,default='')
    Date_of_Baptism=models.DateField(null=True)
    pro=(('Torba','Torba'),
        ('Sanma','Sanma'),
        ('Penama','Penama'),
        ('Malampa','Malampa'),
        ('Shefa','Shefa'),
        ('Tafea','Tafea'),


        )
    Province=models.CharField(max_length=100, choices=pro,blank=True,default='')
    Congregation=models.CharField(max_length=100,default='')
    stat=(
            ('Active','Active'),
            ('Missing','Missing'),
            ('Unknown','Unknow'),
            ('Transfer','Transfer'),

    )

    Status=models.CharField(max_length=100, choices=stat,blank=True,default='')
    Comments=models.TextField(default='')
    def __unicode__(self):
		return self.First_Name


#minutes
class minutes(models.Model):
    date=models.DateField()
    Taken_By=models.CharField(max_length=100)
    Agender=models.CharField(max_length=100)
    body=models.TextField()
    comment=models.TextField(null=True)
    def __unicode__(self):
        return self.Agender

#It will activate whenever you will save file in uploadfolder model
