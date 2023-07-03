from django.contrib import admin
from .models import BoardModel

# Register your models here.
# 「models.py」ファイルにModelを作成したら、ここに記載する
admin.site.register(BoardModel)
