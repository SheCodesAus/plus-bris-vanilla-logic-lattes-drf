# Generated by Django 3.2.5 on 2021-11-27 00:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('canvas', '0008_canvas_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='canvas',
            name='is_public',
            field=models.BooleanField(null=True),
        ),
    ]
