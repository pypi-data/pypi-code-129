# Generated by Django 4.0.2 on 2022-02-09 16:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reduction_viewer', '0014_auto_20211008_1214'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='output',
            name='job',
        ),
        migrations.RemoveField(
            model_name='output',
            name='type',
        ),
        migrations.DeleteModel(
            name='Setting',
        ),
        migrations.AlterField(
            model_name='reductionarguments',
            name='instrument',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='arguments', to='reduction_viewer.instrument'),
        ),
        migrations.AlterField(
            model_name='reductionrun',
            name='overwrite',
            field=models.BooleanField(default=False),
        ),
        migrations.DeleteModel(
            name='Output',
        ),
        migrations.DeleteModel(
            name='OutputType',
        ),
    ]
