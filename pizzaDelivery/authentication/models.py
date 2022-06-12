'''from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.base_user import BaseUserManager

from django.utils.translation import ugettext as _
from phonenumber_field.modelfields import PhoneNumberField
class CustomUserManager(BaseUserManager):
    def create_user(self,email,password, **extra_fields):
        if not email:
            raise ValueError(_('User Must have an email address'))
        
        new_user = self.model(email=self.normalize_email(email),**extra_fields)
        new_user.set_password(password)
        new_user.save(using=self._db)
        return new_user

    def create_superuser(self,email,password, **extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        extra_fields.setdefault('is_active',True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser should have is_staff as True'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_("SuperUser should have is_superuser as True"))
        if extra_fields.get('is_active') is not True:
            raise ValueError(_('SuperUser should have is_active as True'))
        return self.create_user(email,password, **extra_fields)

class User(AbstractBaseUser):
    username = models.CharField(max_length=15, unique=True)
    email = models.EmailField(max_length=30, unique=True)
    phone_number = PhoneNumberField(null=True,unique=True)
    # is_staff = models.BooleanField(default=True)
    # is_active = models.BooleanField(default=True)
    # is_superuser = models.BooleanField(default=True)

    objects =CustomUserManager()
    # USERNAME_FILED='email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','phone_number']

    def __str__(self):
        return f"User {self.email}"

'''
from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from phonenumber_field.modelfields import PhoneNumberField



class CustomUserManager(BaseUserManager):
    def create_user(self, email,username, password=None,):
        if not email:
            raise ValueError('Users must have an email address')
        if not username:
            raise ValueError('Users must have an username address')

        user = self.model(
            email=self.normalize_email(email),username=username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email,username, password=None):
 
        user = self.create_user(
            email,username,
            password
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    username = models.CharField(max_length=15, unique=True)
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    phone_number = PhoneNumberField(null=True,unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username',]

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin