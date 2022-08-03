# Generated by Django 3.0.8 on 2020-07-23 14:20

import uuid

import django.db.models.deletion
import swapper
from django.conf import settings
from django.contrib.auth.management import create_permissions
from django.db import migrations, models

from openwisp_notifications.migrations import get_swapped_model
from openwisp_notifications.types import NOTIFICATION_CHOICES


def create_notification_setting_groups_permissions(apps, schema_editor):
    # Populate permissions
    app_config = apps.get_app_config('openwisp_notifications')
    app_config.models_module = True
    create_permissions(app_config, apps=apps, verbosity=0)
    app_config.models_module = None

    Group = get_swapped_model(apps, 'openwisp_users', 'Group')
    Permission = apps.get_model('auth', 'Permission')

    operator = Group.objects.filter(name='Operator')
    if operator.count() == 0:
        operator = Group.objects.create(name='Operator')
    else:
        operator = operator.first()

    admin = Group.objects.filter(name='Administrator')
    if admin.count() == 0:
        admin = Group.objects.create(name='Administrator')
    else:
        admin = admin.first()

    permissions = [
        Permission.objects.get(
            content_type__app_label='openwisp_notifications',
            content_type__model='notificationsetting',
            codename='change_notificationsetting',
        ).pk,
    ]

    permissions += operator.permissions.all()
    operator.permissions.set(permissions)

    permissions += admin.permissions.all()
    admin.permissions.set(permissions)


def reverse_notification_setting_groups_permissions(apps, schema_editor):
    Group = get_swapped_model(apps, 'openwisp_users', 'Group')
    operator = Group.objects.filter(name='Operator').first()
    administrator = Group.objects.filter(name='Administrator').first()

    if operator is not None:
        operator.permissions.filter(
            content_type__app_label='openwisp_notifications',
            content_type__model='notificationsetting',
        ).delete()
    if administrator is not None:
        administrator.permissions.filter(
            content_type__app_label='openwisp_notifications',
            content_type__model='notificationsetting',
        ).delete()


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        swapper.dependency('openwisp_users', 'Organization'),
        ('openwisp_notifications', '0003_notification_notification_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='NotificationSetting',
            fields=[
                (
                    'id',
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    'type',
                    models.CharField(
                        choices=NOTIFICATION_CHOICES,
                        max_length=30,
                        null=True,
                        verbose_name='Notification Type',
                    ),
                ),
                (
                    'web',
                    models.BooleanField(
                        null=True,
                        blank=True,
                        help_text=(
                            'Note: Non-superadmin users receive notifications only '
                            'for organizations of which they are member of.'
                        ),
                        verbose_name='web notifications',
                    ),
                ),
                (
                    'email',
                    models.BooleanField(
                        null=True,
                        blank=True,
                        help_text=(
                            'Note: Non-superadmin users receive notifications only '
                            'for organizations of which they are member of.'
                        ),
                        verbose_name='email notifications',
                    ),
                ),
                (
                    'organization',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=swapper.get_model_name('openwisp_users', 'Organization'),
                    ),
                ),
                (
                    'user',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                'verbose_name': 'user notification settings',
                'verbose_name_plural': 'user notification settings',
                'ordering': ['organization', 'type'],
                'abstract': False,
                'swappable': 'OPENWISP_NOTIFICATIONS_NOTIFICATIONSETTING_MODEL',
            },
        ),
        migrations.AddConstraint(
            model_name='notificationsetting',
            constraint=models.UniqueConstraint(
                fields=('organization', 'type', 'user'),
                name='unique_notification_setting',
            ),
        ),
        migrations.AddIndex(
            model_name='notificationsetting',
            index=models.Index(
                fields=['type', 'organization'], name='openwisp_no_type_5a6a77_idx'
            ),
        ),
        migrations.RunPython(
            create_notification_setting_groups_permissions,
            reverse_code=reverse_notification_setting_groups_permissions,
        ),
    ]
