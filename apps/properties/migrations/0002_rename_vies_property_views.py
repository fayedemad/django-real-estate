# Generated by Django 3.2.7 on 2023-03-02 20:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='property',
            old_name='vies',
            new_name='views',
        ),
    ]
