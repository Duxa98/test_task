# Generated by Django 2.2.3 on 2019-07-13 15:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_list', '0012_auto_20190713_1441'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='appuser',
            options={'ordering': ['login'], 'verbose_name': 'AppUser', 'verbose_name_plural': 'AppUsers'},
        ),
        migrations.AlterModelOptions(
            name='token',
            options={'ordering': ['token'], 'verbose_name': 'Token', 'verbose_name_plural': 'Tokens'},
        ),
        migrations.AlterModelTable(
            name='appuser',
            table='appuser',
        ),
        migrations.AlterModelTable(
            name='token',
            table='token',
        ),
    ]
