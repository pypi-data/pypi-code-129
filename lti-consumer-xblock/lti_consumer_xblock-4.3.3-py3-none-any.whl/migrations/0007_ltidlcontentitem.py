# Generated by Django 2.2.17 on 2021-01-26 19:12

from django.db import migrations, models
import django.db.models.deletion
import jsonfield.encoder
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('lti_consumer', '0006_add_on_model_config_for_lti_1p1'),
    ]

    operations = [
        migrations.CreateModel(
            name='LtiDlContentItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content_type', models.CharField(choices=[('link', 'Link to external resource'), ('ltiResourceLink', 'LTI Resource Link'), ('file', 'File'), ('html', 'HTML Fragment'), ('image', 'Image')], max_length=255)),
                ('attributes', jsonfield.fields.JSONField(dump_kwargs={'cls': jsonfield.encoder.JSONEncoder, 'separators': (',', ':')}, load_kwargs={})),
                ('lti_configuration', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='lti_consumer.LtiConfiguration')),
            ],
        ),
    ]
