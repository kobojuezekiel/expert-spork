# Generated by Django 3.2.4 on 2021-11-01 12:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Thread',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('html_id', django_extensions.db.fields.RandomCharField(blank=True, editable=False, length=10)),
                ('thread_type', models.CharField(choices=[('personal', 'Personal'), ('group', 'Group')], max_length=40)),
                ('last_activity', models.DateTimeField(auto_now=True)),
                ('users', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-last_activity'],
            },
        ),
        migrations.CreateModel(
            name='ChatMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('read', models.BooleanField(default=False)),
                ('time_stamp', models.DateTimeField(auto_now=True)),
                ('sender', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('thread', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chat.thread')),
            ],
        ),
    ]