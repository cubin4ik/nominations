from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    class Colors(models.TextChoices):
        BLUE = "BLU", "#99b6ff"
        PINK = "PNK", "#ff99cc"
        BROWN = "BRW", "#ffa399"
        GREEN = "GRN", "#4ff965"
        VIOLET = "VLT", "#eb99ff"
        YELLOW = "YLW", "#99a9ff"

    color = models.CharField(max_length=3, choices=Colors.choices, default=Colors.BLUE)
