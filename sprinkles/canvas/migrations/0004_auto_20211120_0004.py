# Generated by Django 3.2.5 on 2021-11-20 00:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('canvas', '0003_auto_20211116_1013'),
    ]

    operations = [
        migrations.RenameField(
            model_name='canvas',
            old_name='user',
            new_name='owner',
        ),
        migrations.RenameField(
            model_name='stickynote',
            old_name='user',
            new_name='owner',
        ),
    ]