from django.db import models

# Create your models here.
class User_Info(models.Model):
    uid = models.CharField(max_length=50,null=False,default='')         #user_id
    name = models.CharField(max_length=255,blank=True,null=False)       #LINE名字
    pic_url = models.CharField(max_length=255,null=False)               #大頭貼網址
    mtext = models.CharField(max_length=255,blank=True,null=False)      #文字訊息紀錄
    mdt = models.DateTimeField(auto_now=True)                           #物件儲存的日期時間
    stage = models.CharField(max_length=50,null=False,default='尚未建立會員')

    def __str__(self):
        return self.uid

class Hotpot(models.Model):
    student_id = models.CharField(max_length=20)
    getpoint = models.IntegerField(default=0)

class Github(models.Model):
    student_id = models.CharField(max_length=20)
    getpoint = models.IntegerField(default=0)

class Sheet(models.Model):
    student_id = models.CharField(max_length=20)
    getpoint = models.IntegerField(default=0)

class Machi(models.Model):
    student_id = models.CharField(max_length=20)
    getpoint = models.IntegerField(default=0)
class Jolin(models.Model):
    student_id = models.CharField(max_length=20)
    getpoint = models.IntegerField(default=0)
    flg = models.BooleanField(default=0)
