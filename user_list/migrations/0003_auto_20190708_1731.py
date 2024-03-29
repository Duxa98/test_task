# Generated by Django 2.2.3 on 2019-07-08 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_list', '0002_auto_20190708_1729'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appuser',
            name='birthday',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='appuser',
            name='creation_time',
            field=models.FloatField(default=1562607113.659116, editable=False),
        ),
        migrations.AlterField(
            model_name='appuser',
            name='food_preferences',
            field=models.CharField(choices=[('M1', 'menu1'), ('M2', 'menu2'), ('M3', 'menu3')], default='M1', max_length=32),
        ),
        migrations.AlterField(
            model_name='appuser',
            name='update_time',
            field=models.FloatField(default=1562607113.659129),
        ),
        migrations.AlterField(
            model_name='appuser',
            name='weight',
            field=models.FloatField(default=0),
        ),
    ]
