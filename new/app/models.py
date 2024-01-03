from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class contact(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    subject=models.CharField(max_length=50)
    پیام = models.TextField()


class resume(models.Model):
    # projectName= models.CharField(max_length=100)
    # employer= models.CharField(max_length=500)
    # ProjectSize= models.CharField(max_length=100)
    # date= models.CharField(max_length=10)
    Resume=RichTextUploadingField()
    pub_date = models.DateTimeField(auto_now_add= True)
    last_edited= models.DateTimeField(auto_now= True)
    # def __str__(self):
    #     return self.title