# Generated by Django 2.2.24 on 2022-03-24 02:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20220323_2340'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='is_active',
            new_name='is_activate',
        ),
    ]