# Generated by Django 4.0.3 on 2022-04-01 19:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Idea',
            fields=[
                ('idea_id', models.UUIDField(default=uuid.UUID('4c67532c-2e2c-4aec-b130-80e8e05a2554'), editable=False, primary_key=True, serialize=False, unique=True, verbose_name='Idea ID')),
                ('title', models.CharField(max_length=500, unique=True)),
                ('details', models.TextField(editable=False, unique=True)),
                ('date_time_created', models.DateTimeField(auto_now=True, verbose_name='Date and time created')),
                ('tags', models.JSONField()),
                ('repository_link', models.TextField(blank=True, null=True, unique=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
