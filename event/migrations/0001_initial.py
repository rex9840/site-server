# Generated by Django 5.1.1 on 2024-10-29 08:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Event",
            fields=[
                (
                    "slug",
                    models.SlugField(
                        editable=False,
                        max_length=350,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("title", models.CharField(max_length=400)),
                ("start_date", models.DateField()),
                ("end_date", models.DateField()),
                ("description", models.TextField()),
                (
                    "rsvp_url",
                    models.URLField(blank=True, max_length=500, null=True),
                ),
                (
                    "add_to_calender_url",
                    models.URLField(blank=True, max_length=500, null=True),
                ),
                ("is_draft", models.BooleanField(default=False)),
                ("max_capacity", models.IntegerField()),
                ("price", models.IntegerField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("registration_deadline", models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name="EventLocation",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=150)),
                (
                    "google_maps_location",
                    models.URLField(blank=True, max_length=500, null=True),
                ),
            ],
        ),
        migrations.CreateModel(
            name="EventType",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name="HotTopic",
            fields=[
                (
                    "name",
                    models.CharField(
                        max_length=100, primary_key=True, serialize=False
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Speaker",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("profession", models.CharField(max_length=255)),
                ("twitter", models.URLField(max_length=255)),
                ("linkedin", models.URLField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="EventImage",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("caption", models.TextField(blank=True, null=True)),
                ("image", models.ImageField(upload_to="")),
                ("position", models.IntegerField(default=1)),
                ("published", models.BooleanField(default=False)),
                (
                    "event",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="event_images",
                        to="event.event",
                    ),
                ),
            ],
            options={
                "ordering": ["position"],
            },
        ),
        migrations.AddField(
            model_name="event",
            name="location",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="event.eventlocation",
            ),
        ),
        migrations.AddField(
            model_name="event",
            name="event_type",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="event.eventtype",
            ),
        ),
        migrations.AddField(
            model_name="event",
            name="hot_topics",
            field=models.ManyToManyField(
                related_name="events",
                related_query_name="events",
                to="event.hottopic",
            ),
        ),
        migrations.CreateModel(
            name="Schedule",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "title",
                    models.CharField(blank=True, max_length=250, null=True),
                ),
                ("start_time", models.CharField(max_length=100)),
                ("end_time", models.CharField(max_length=100)),
                ("emoji", models.CharField(max_length=2)),
                (
                    "event",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="schedules",
                        to="event.event",
                    ),
                ),
                ("speakers", models.ManyToManyField(to="event.speaker")),
            ],
        ),
    ]