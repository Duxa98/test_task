# Generated by Django 2.2.3 on 2019-07-13 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_list', '0009_auto_20190713_1249'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Token',
            new_name='tokens',
        ),
        migrations.AlterField(
            model_name='appuser',
            name='creation_time',
            field=models.FloatField(default=1563022362.9527, editable=False),
        ),
        migrations.AlterField(
            model_name='appuser',
            name='update_time',
            field=models.FloatField(default=1563022362.952713, editable=False),
        ),
    ]