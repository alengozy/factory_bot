from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
# Create your models here.


class CustomUserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, name, password=None, **extra_fields):
        if not name:
            raise ValueError('Users must have a name')
        user = self.model(self, name=name **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, name, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(name, password, **extra_fields)
        


class CustomUser(AbstractUser):
    username = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100)
    email = None
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.name

