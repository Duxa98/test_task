# Generated by Django 2.2.3 on 2019-07-13 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_list', '0006_auto_20190713_1159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appuser',
            name='creation_time',
            field=models.FloatField(default=1563019231.29936, editable=False),
        ),
        migrations.AlterField(
            model_name='appuser',
            name='update_time',
            field=models.FloatField(default=1563019231.299372, editable=False),
        ),
    ]
