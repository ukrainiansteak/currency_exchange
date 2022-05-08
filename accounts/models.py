from django.contrib.auth.models import AbstractUser
from django.core.validators import FileExtensionValidator, RegexValidator
from django.db import models


class Profile(AbstractUser):
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    email = models.EmailField(
        unique=True
    )
    phone_number = models.CharField(
        null=True,
        max_length=24,
        validators=[
            RegexValidator(r'^(\+\d\d?)\d{10}$',
                           message="Phone should be in format +11112223344")
        ])
    image = models.ImageField(
        null=True,
        upload_to='pics/',
        blank=True,
        validators=[
            FileExtensionValidator(['jpg', 'png'])
        ]
    )
