from django.contrib import admin
from .models import UserModel
from django.contrib.auth.admin import UserAdmin

# Register your models here.
admin.site.register(UserModel, UserAdmin) # 이 코드가 나의 UserModel을 Admin에 추가 해 줍니다
