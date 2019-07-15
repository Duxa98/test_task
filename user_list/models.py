from django.db import models
import uuid

# Create your models here.

FOOD_PREFERENCES = [
    ('M1', 'menu1'),
    ('M2', 'menu2'),
    ('M3', 'menu3')
]


class AppUser(models.Model):
    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  # ,unique=True)
    login = models.CharField(null=False, unique=True, max_length=32)
    weight = models.FloatField(null=True, default=0)
    birthday = models.DateField(null=True)
    creation_time = models.DateTimeField(auto_now_add=True, editable=False)  # TODO: goto timestamp
    update_time = models.DateTimeField(auto_now=True, editable=False)  # TODO: goto timestamp
    food_preferences = models.CharField(null=True, default='M1', choices=FOOD_PREFERENCES, max_length=32)

    class Meta:
        verbose_name = 'AppUser'
        verbose_name_plural = 'AppUsers'
        ordering = ['login']
        db_table = 'appuser'


    def save(self, **kwargs):
        super().save(**kwargs)
        token = f'{self.login}_token'
        Token(user=self, token=token).save()

    def __str__(self):
        return f'{self.login}'


class Token(models.Model):
    token_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  # , unique=True)
    user = models.OneToOneField(to=AppUser, on_delete=models.CASCADE, related_name='token')
    token = models.TextField(null=False, max_length=32, unique=True)

    class Meta:
        verbose_name = 'Token'
        verbose_name_plural = 'Tokens'
        ordering = ['token']
        db_table = 'token'

    def __str__(self):
        return f'{self.token}'
