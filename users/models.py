from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):

    """ Custom User Model """

    GENDER_MALE = "Male"
    GENDER_FEMALE = "Female"
    GENDER_OTHER = "Other"

    GENDER_CHOICES = (
        (GENDER_MALE, "Mail"),
        (GENDER_FEMALE, "Femail"),
        (GENDER_OTHER, "Other"),
    )

    LANGUAGE_ENGLISH = "english"
    LANGUAGE_KOREAN = "korean"

    LANGUAGE_CHOICE = ((LANGUAGE_ENGLISH, "EN"), (LANGUAGE_KOREAN, "KR"))

    CURRENCY_USD = "usd"
    CURRENCY_KRW = "krw"

    CURRENCY_CHOICE = ((CURRENCY_USD, "USD"), (CURRENCY_KRW, "KRW"))

    avatar = models.ImageField(upload_to="avatar", blank=True)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=10, blank=True)
    bio = models.TextField(blank=True)
    birthday = models.DateField(blank=True, null=True)
    langauge = models.CharField(choices=LANGUAGE_CHOICE, max_length=6, blank=True)
    currency = models.CharField(choices=CURRENCY_CHOICE, max_length=3, blank=True)
    superhost = models.BooleanField(default=False)
