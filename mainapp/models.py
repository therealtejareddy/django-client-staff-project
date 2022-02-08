from time import time
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Member(models.Model):
    user = models.OneToOneField(User,null=True, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.user)


class Client(models.Model):
    member = models.ForeignKey(Member, null=True, on_delete=models.SET_NULL)
    time = models.DateTimeField(auto_now_add=True)
    file = models.FileField(null=True,upload_to='files')

    def __str__(self):
        return str(self.time)

class Staff(models.Model):
    time = models.DateTimeField(auto_now_add=True)
    file = models.FileField(null=True,upload_to="files")
    file_num = models.IntegerField(null=True)
    num_of_mails = models.IntegerField(null=True)