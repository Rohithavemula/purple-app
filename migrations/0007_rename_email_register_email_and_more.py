# Generated by Django 5.0.6 on 2024-06-22 08:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0006_delete_login'),
    ]

    operations = [
        migrations.RenameField(
            model_name='register',
            old_name='email',
            new_name='Email',
        ),
        migrations.RenameField(
            model_name='register',
            old_name='fullname',
            new_name='Fullname',
        ),
        migrations.RenameField(
            model_name='register',
            old_name='mobilenumber',
            new_name='Mobilenumber',
        ),
        migrations.RenameField(
            model_name='register',
            old_name='password',
            new_name='Password',
        ),
    ]
