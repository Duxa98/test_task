# Generated by Django 2.2.3 on 2019-07-15 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_list', '0024_auto_20190715_1252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appuser',
            name='weight',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=3),
        ),
    ]
