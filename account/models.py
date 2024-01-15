from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import Q
from django.core.validators import MinLengthValidator, RegexValidator

class Account(AbstractUser):
    class Meta:
        db_table = "account"
        managed = True
        constraints = [models.UniqueConstraint(fields=["email", "is_deleted"], condition=Q(is_deleted=False), name="unique_active_email")]

    class Gender(models.TextChoices):
        MALE = "Male",
        FEMALE = "Female",
        TRANSGENDER = "Transgender",
        BINARY = "Binary",
        PREFER_NOT_TO_SAY = "Prefer not to say"

    full_name = models.CharField(db_column='full_name', max_length=255, validators=[MinLengthValidator(3)])
    email = models.EmailField(db_column='email', max_length=100)
    password = models.CharField(db_column='password', max_length=1000)
    phone_number = models.CharField(db_column='phone_number', max_length=20)
    address = models.TextField(max_length=1000)
    gender = models.CharField(max_length=20, choices=Gender.choices)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    username=None
    first_name = None
    last_name = None
    is_superuser = None
    last_login = None
    date_joined = None
    is_staff = None
    is_active = True

    USERNAME_FIELD  = 'id'
    REQUIRED_FIELDS = []


    account_repository = models.Manager()
