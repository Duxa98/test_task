# Generated by Django 2.2.3 on 2019-07-13 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_list', '0008_auto_20190713_1216'),
    ]

    operations = [
        migrations.RenameField(
            model_name='token',
            old_name='user_id',
            new_name='user',
        ),
        migrations.AlterField(
            model_name='appuser',
            name='creation_time',
            field=models.FloatField(default=1563022147.417091, editable=False),
        ),
        migrations.AlterField(
            model_name='appuser',
            name='update_time',
            field=models.FloatField(default=1563022147.417104, editable=False),
        ),
    ]
