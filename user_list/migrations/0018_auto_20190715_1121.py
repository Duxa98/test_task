# Generated by Django 2.2.3 on 2019-07-15 11:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_list', '0017_auto_20190715_1100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='token',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='token', to='user_list.AppUser'),
        ),
    ]