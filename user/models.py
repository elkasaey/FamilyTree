from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, username, password,name):
        if not username:
            raise ValueError('User must have an username')

        user = self.model(username=username,name)
        user.set_password(password)
        user.save()
        return user

class User(AbstractBaseUser):
    username = models.CharField(max_length=150, unique = True)
    name = models.CharField(max_length = 80)
    createdAt = models.DateTimeField(auto_now_add=True)

    objects = UserManager()
    USERNAME_FIELD = 'username'
