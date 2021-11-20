# Generated by Django 3.2.5 on 2021-11-16 10:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('canvas', '0002_canvas_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='canvas',
            old_name='is_open',
            new_name='is_public',
        ),
        migrations.RemoveField(
            model_name='canvas',
            name='image',
        ),
        migrations.CreateModel(
            name='StickyNote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('who', models.TextField()),
                ('what', models.TextField()),
                ('why', models.TextField()),
                ('anonymous', models.BooleanField()),
                ('canvas', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sticky_notes', to='canvas.canvas')),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]