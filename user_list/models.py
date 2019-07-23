from django.db import models
import uuid

# from unixtimestampfield.fields import UnixTimeStampField

# Create your models here.

FOOD_PREFERENCES = [
    ('M1', 'menu1'),
    ('M2', 'menu2'),
    ('M3', 'menu3')
]


class AppUser(models.Model):
    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    login = models.CharField(null=False, unique=True, max_length=32)
    weight = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    birthday = models.DateField(null=True)
    creation_time = models.DateTimeField(auto_now_add=True, editable=False)
    update_time = models.DateTimeField(auto_now=True, editable=False)
    # creation_time = UnixTimeStampField(use_numeric=True, auto_now_add=True, editable=False)
    # update_time = UnixTimeStampField(use_numeric=True, auto_now=True, editable=False)
    food_preferences = models.CharField(default='M1', choices=FOOD_PREFERENCES, max_length=32)

    class Meta:
        verbose_name = 'AppUser'
        verbose_name_plural = 'AppUsers'
        ordering = ['login']
        db_table = 'appuser'

    def save(self, **kwargs):
        super().save(**kwargs)
        token = f'{self.login}_token'
        if not MyToken.objects.filter(token=token).exists():
            MyToken(user=self, token=token).save()

    def __str__(self):
        return f'{self.login}'


class MyToken(models.Model):
    token_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(to=AppUser, on_delete=models.CASCADE, related_name='token')
    token = models.TextField(null=False, max_length=32, unique=True)

    class Meta:
        verbose_name = 'Token'
        verbose_name_plural = 'Tokens'
        ordering = ['token']
        db_table = 'token'

    def __str__(self):
        return f'{self.token}'
