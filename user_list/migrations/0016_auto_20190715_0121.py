# Generated by Django 2.2.3 on 2019-07-15 01:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_list', '0015_auto_20190714_1754'),
    ]

    operations = [
        migrations.AlterField(
            model_name='token',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_items', to='user_list.AppUser'),
        ),
    ]
