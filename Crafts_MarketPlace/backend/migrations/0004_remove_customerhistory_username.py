# Generated by Django 4.0.5 on 2022-06-26 04:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_alter_customerhistory_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customerhistory',
            name='username',
        ),
    ]
