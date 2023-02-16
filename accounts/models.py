from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    # is_teacher = models.BooleanField('teacher status', default=False)
    # is_student = models.BooleanField('student status', default=True)
    USER_TYPE_CHOICE = (
        (1, "student"),
        (2, "teacher"),
    )

    user_type = models.PositiveBigIntegerField(choices=USER_TYPE_CHOICE)
    codico_criacao_teacher = models.IntegerField()