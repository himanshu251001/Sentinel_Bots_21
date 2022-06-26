# Generated by Django 4.0.5 on 2022-06-26 05:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('backend', '0009_remove_sellerdata_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sellerdata',
            name='username',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]