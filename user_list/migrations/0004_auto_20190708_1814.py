# Generated by Django 2.2.3 on 2019-07-08 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_list', '0003_auto_20190708_1731'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appuser',
            name='creation_time',
            field=models.FloatField(default=1562609683.954875, editable=False),
        ),
        migrations.AlterField(
            model_name='appuser',
            name='update_time',
            field=models.FloatField(default=1562609683.954888),
        ),
    ]
