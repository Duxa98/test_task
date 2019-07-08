from django.db import models

# Create your models here.

FOOD_PREFERENCES = ['menu1', 'menu2', 'menu3']

class AppUser(models.Model):
    user_id = models.IntegerField(primary_key=True)
    login = models.CharField(unique=True)
    weigth = models.FloatField()
    birthday = models.DateField()
    creation_time = models.DateTimeField()
    update_time = models.DateTimeField()
    food_preferences = models.CharField(choices=FOOD_PREFERENCES)

    def __str__(self):
        return f'{self.login}, {self.food_preferences}'


class tokens(models.Model):
    token_id = models.IntegerField(primary_key=True)
    user_id = models.ForeignKey(to=AppUser, on_delete=models.CASCADE, related_name='user_token')
    token = models.CharField(null=False)
