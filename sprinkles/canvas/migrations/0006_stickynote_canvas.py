# Generated by Django 3.2.5 on 2021-11-20 01:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('canvas', '0005_remove_stickynote_canvas'),
    ]

    operations = [
        migrations.AddField(
            model_name='stickynote',
            name='canvas',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='sticky_notes', to='canvas.canvas'),
            preserve_default=False,
        ),
    ]
