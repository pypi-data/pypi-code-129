# Generated by Django 3.2.6 on 2022-02-13 16:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('podcasts', '0009_auto_20220213_1407'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('remote_id', models.CharField(editable=False, max_length=255)),
                ('country', models.CharField(max_length=50, null=True)),
                ('title', models.CharField(max_length=255)),
                ('body', models.TextField(blank=True, null=True)),
                ('author', models.CharField(max_length=50)),
                ('published', models.DateTimeField()),
                ('rating', models.DecimalField(decimal_places=1, max_digits=2, null=True)),
                ('approved', models.BooleanField(null=True)),
                ('directory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='podcasts.directory')),
                ('podcast', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='podcasts.podcast')),
            ],
            options={
                'ordering': ('-published',),
                'get_latest_by': 'published',
                'unique_together': {('remote_id', 'directory', 'podcast')},
            },
        ),
    ]
