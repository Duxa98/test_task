import datetime

from django.db import models
import uuid

# Create your models here.

FOOD_PREFERENCES = [
    ('M1', 'menu1'),
    ('M2', 'menu2'),
    ('M3', 'menu3')
]


class AppUser(models.Model):
    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  # , unique=True)
    login = models.CharField(null=False, unique=True, max_length=32)
    weight = models.FloatField(null=True, default=0)
    birthday = models.DateField(null=True)
    creation_time = models.FloatField(default=datetime.datetime.now().timestamp(), editable=False)
    update_time = models.FloatField(default=datetime.datetime.now().timestamp())
    food_preferences = models.CharField(null=True, default='M1', choices=FOOD_PREFERENCES, max_length=32)

    def __str__(self):
        return f'{self.login}, {self.food_preferences}'


class tokens(models.Model):
    token_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  # , unique=True)
    user_id = models.ForeignKey(to=AppUser, on_delete=models.CASCADE, related_name='user_token')
    token = models.CharField(null=False, max_length=32)

    def __str__(self):
        return f'{self.token}'
