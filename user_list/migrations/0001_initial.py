# Generated by Django 2.2.3 on 2019-07-08 17:23

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AppUser',
            fields=[
                ('user_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('login', models.CharField(max_length=32, unique=True)),
                ('weigth', models.FloatField()),
                ('birthday', models.DateField()),
                ('creation_time', models.FloatField(default=1562606623.472797, editable=False)),
                ('update_time', models.FloatField(default=1562606623.47281)),
                ('food_preferences', models.CharField(choices=[('M1', 'menu1'), ('M2', 'menu2'), ('M3', 'menu3')], max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='tokens',
            fields=[
                ('token_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('token', models.CharField(max_length=32)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_token', to='user_list.AppUser')),
            ],
        ),
    ]
