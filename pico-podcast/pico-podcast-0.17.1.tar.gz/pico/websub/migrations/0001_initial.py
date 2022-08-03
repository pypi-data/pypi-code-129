# Generated by Django 3.2 on 2022-02-05 12:49

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('hub', models.URLField(max_length=512)),
                ('topic', models.URLField(max_length=512)),
                ('lease_seconds', models.PositiveIntegerField(null=True)),
                ('secret', models.CharField(max_length=64)),
                ('confirmed', models.DateTimeField(editable=False, null=True)),
                ('expires', models.DateTimeField(editable=False, null=True)),
            ],
            options={
                'unique_together': {('topic', 'hub')},
            },
        ),
    ]
