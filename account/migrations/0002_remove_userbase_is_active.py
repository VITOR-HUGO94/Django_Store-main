# Generated by Django 2.2.24 on 2022-01-30 17:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userbase',
            name='is_active',
        ),
    ]