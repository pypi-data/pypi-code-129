# Generated by Django 2.1.3 on 2018-12-05 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [('connection', '0001_initial')]

    operations = [
        migrations.AddField(
            model_name='credentials',
            name='auto_add',
            field=models.BooleanField(
                default=False,
                help_text=(
                    'automatically add these credentials to the '
                    'devices of this organization; if no organization is '
                    'specified will be added to all the new devices'
                ),
                verbose_name='auto add',
            ),
        )
    ]
