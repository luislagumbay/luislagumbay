from django.contrib.auth.models import AbstractUser, BaseUserManager, Group, Permission
from django.db import models
from django.conf import settings

class UserManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError("Users must have an email address")
        user = self.model(email=self.normalize_email(email), username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user

class User(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=30, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    groups = models.ManyToManyField(
        Group,
        related_name='custom_user_set',  # Unique related name to avoid clashes
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_permissions_set',  # Unique related name to avoid clashes
        blank=True,
    )
    def __str__(self):
        return self.email

    class Meta:
        app_label = 'account'  # Explicitly declare the app label

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    weight = models.FloatField()
    height = models.FloatField()
    region = models.CharField(max_length=100)
    province = models.CharField(max_length=100)
    municipality = models.CharField(max_length=100)
    blood_type = models.CharField(max_length=3)
    availability = models.BooleanField(default=False)
    last_donation_date = models.DateField(null=True, blank=True)

    class Meta:
        db_table = 'account_profile'

    def __str__(self):
        return f"{self.user.username}'s Profile"
