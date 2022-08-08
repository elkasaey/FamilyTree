from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, username, password, **other_fields):
        if not username:
            raise ValueError('User must have an username')

        user = self.model(username=username, **other_fields)
        user.set_password(password)
        user.save()
        return user

class Gender(models.Model):
    name = models.CharField(max_length=20, unique = True)

class User(AbstractBaseUser):
    username = models.CharField(max_length=150, unique = True)
    name = models.CharField(max_length = 80)
    gender = models.ForeignKey(Gender,on_delete=models.DO_NOTHING)
    createdAt = models.DateTimeField(auto_now_add=True)

    objects = UserManager()
    USERNAME_FIELD = 'username'
