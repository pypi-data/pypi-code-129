# Generated by Django 3.0.6 on 2020-05-29 20:38

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Drip",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date", models.DateTimeField(auto_now_add=True)),
                ("lastchanged", models.DateTimeField(auto_now=True)),
                (
                    "name",
                    models.CharField(
                        help_text="A unique name for this drip.",
                        max_length=255,
                        unique=True,
                        verbose_name="Drip Name",
                    ),
                ),
                ("enabled", models.BooleanField(default=False)),
                (
                    "from_email",
                    models.EmailField(
                        blank=True,
                        help_text="Set a custom from email.",
                        max_length=254,
                        null=True,
                    ),
                ),
                (
                    "from_email_name",
                    models.CharField(
                        blank=True,
                        help_text="Set a name for a custom from email.",
                        max_length=150,
                        null=True,
                    ),
                ),
                ("subject_template", models.TextField(blank=True, null=True)),
                (
                    "body_html_template",
                    models.TextField(
                        blank=True,
                        help_text="You will have settings and user in the context.",
                        null=True,
                    ),
                ),
                (
                    "message_class",
                    models.CharField(blank=True, default="default", max_length=120),
                ),
            ],
        ),
        migrations.CreateModel(
            name="SentDrip",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date", models.DateTimeField(auto_now_add=True)),
                ("subject", models.TextField()),
                ("body", models.TextField()),
                (
                    "from_email",
                    models.EmailField(default=None, max_length=254, null=True),
                ),
                (
                    "from_email_name",
                    models.CharField(default=None, max_length=150, null=True),
                ),
                (
                    "drip",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="sent_drips",
                        to="drip.Drip",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="sent_drips",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="QuerySetRule",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date", models.DateTimeField(auto_now_add=True)),
                ("lastchanged", models.DateTimeField(auto_now=True)),
                (
                    "method_type",
                    models.CharField(
                        choices=[("filter", "Filter"), ("exclude", "Exclude")],
                        default="filter",
                        max_length=12,
                    ),
                ),
                (
                    "field_name",
                    models.CharField(max_length=128, verbose_name="Field name of User"),
                ),
                (
                    "lookup_type",
                    models.CharField(
                        choices=[
                            ("exact", "exactly"),
                            ("iexact", "exactly (case insensitive)"),
                            ("contains", "contains"),
                            ("icontains", "contains (case insensitive)"),
                            ("regex", "regex"),
                            ("iregex", "contains (case insensitive)"),
                            ("gt", "greater than"),
                            ("gte", "greater than or equal to"),
                            ("lt", "less than"),
                            ("lte", "less than or equal to"),
                            ("startswith", "starts with"),
                            ("endswith", "starts with"),
                            ("istartswith", "ends with (case insensitive)"),
                            ("iendswith", "ends with (case insensitive)"),
                        ],
                        default="exact",
                        max_length=12,
                    ),
                ),
                (
                    "field_value",
                    models.CharField(
                        help_text="Can be anything from a number, to a string. Or, do `now-7 days` or `today+3 days` for fancy timedelta.",
                        max_length=255,
                    ),
                ),
                (
                    "drip",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="queryset_rules",
                        to="drip.Drip",
                    ),
                ),
            ],
        ),
    ]
