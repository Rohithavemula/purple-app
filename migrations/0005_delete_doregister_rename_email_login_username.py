# Generated by Django 5.0.6 on 2024-06-22 06:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_doregister_login'),
    ]

    operations = [
        migrations.DeleteModel(
            name='doregister',
        ),
        migrations.RenameField(
            model_name='login',
            old_name='email',
            new_name='username',
        ),
    ]
