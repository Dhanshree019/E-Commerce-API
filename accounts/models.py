from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin
from django.utils.translation import gettext_lazy
# Create your models here.


class CustomAccountManager(BaseUserManager):
    def create_superuser(self,email=None, password=None, **other_fields):
        other_fields.setdefault('is_admin',True)
        other_fields.setdefault('is_superuser',True)

        if other_fields.get('is_admin') is not True:
            raise ValueError('Superuser must be assigned to is_admin=True.')

        if other_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must be assigned to is_superuser=True.')

        return self.create_user(email, password, **other_fields)

    def create_user(self, email=None, password=None, **other_fields):
        if email is None :
            raise ValueError(gettext_lazy('You must provide an email'))
        user = self.model(email=email, **other_fields)

        if password is not None:
            user.set_password(password)

        user.save()
        return user


class CustomUser(AbstractBaseUser,PermissionsMixin):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    is_admin = models.BooleanField(default=False)

    # timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = CustomAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


    class Meta:
        db_table = 'user'

    def __str__(self):
        return self.email
