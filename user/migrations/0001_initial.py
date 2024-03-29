# Generated by Django 2.2.2 on 2019-06-05 00:21

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LoginModel',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=300)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('user_type', models.IntegerField(choices=[(1, 'Administrator'), (2, 'Moderator'), (3, 'Author')])),
                ('status', models.IntegerField(choices=[(0, 'Inactive'), (1, 'Active')])),
                ('date_joined', models.DateField(auto_now_add=True)),
                ('last_login', models.DateTimeField()),
            ],
            options={
                'db_table': 'logins',
            },
            managers=[
                ('manage', django.db.models.manager.Manager()),
            ],
        ),
    ]
