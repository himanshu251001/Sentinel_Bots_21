# Generated by Django 4.0.5 on 2022-06-26 03:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_customerhistory_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerhistory',
            name='username',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='backend.customerdata'),
        ),
    ]
