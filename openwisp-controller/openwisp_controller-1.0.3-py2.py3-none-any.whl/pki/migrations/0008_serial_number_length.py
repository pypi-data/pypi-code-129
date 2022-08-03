# Generated by Django 3.0.2 on 2020-02-05 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [('pki', '0007_default_groups_permissions')]

    operations = [
        migrations.AlterField(
            model_name='ca',
            name='serial_number',
            field=models.CharField(
                blank=True,
                help_text='leave blank to determine automatically',
                max_length=48,
                null=True,
                verbose_name='serial number',
            ),
        ),
        migrations.AlterField(
            model_name='cert',
            name='serial_number',
            field=models.CharField(
                blank=True,
                help_text='leave blank to determine automatically',
                max_length=48,
                null=True,
                verbose_name='serial number',
            ),
        ),
    ]
