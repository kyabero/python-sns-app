from django.db import models

# Create your models here.

class BoardModel(models.Model): # 以下にフィールドを記載
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.CharField(max_length=50)
    snsimage = models.ImageField(upload_to='')
    good = models.IntegerField(null=True, blank=True, default=1)
    read = models.IntegerField(null=True, blank=True, default=1)
    readtext = models.TextField(null=True, blank=True, default='a')
    
# null,blank = True にすることによって空でも受け付けれるようになる
# default は初めに入力されている値