# Generated by Django 2.2.15 on 2020-08-03 09:49

from django.db import migrations
import django_intenum
import hearthstone.enums


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0003_auto_20190701_1420'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='multi_class_group',
            field=django_intenum.IntEnumField(default=0, enum=hearthstone.enums.MultiClassGroup),
        ),
    ]
