# Generated by Django 2.2.3 on 2019-07-15 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_list', '0022_auto_20190715_1247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appuser',
            name='food_preferences',
            field=models.CharField(choices=[('M1', 'menu1'), ('M2', 'menu2'), ('M3', 'menu3')], default='M1', max_length=32, null=True),
        ),
    ]
