# Generated by Django 2.2.3 on 2019-07-14 17:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_list', '0013_auto_20190713_1507'),
    ]

    operations = [
        migrations.AlterField(
            model_name='token',
            name='token',
            field=models.TextField(max_length=32, unique=True),
        ),
        migrations.AlterField(
            model_name='token',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to='user_list.AppUser'),
        ),
    ]
