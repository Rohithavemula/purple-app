# Generated by Django 5.0.6 on 2024-06-22 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_register_desig'),
    ]

    operations = [
        migrations.CreateModel(
            name='doregister',
            fields=[
                ('fullname', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=15)),
                ('address', models.CharField(max_length=100)),
                ('mobilenumber', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='login',
            fields=[
                ('email', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=15)),
            ],
        ),
    ]
