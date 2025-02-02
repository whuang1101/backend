# Generated by Django 4.2.14 on 2024-07-19 16:04

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("comments", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="comments",
            name="author",
            field=models.CharField(default="wilson", max_length=100),
        ),
        migrations.AddField(
            model_name="comments",
            name="date",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
    ]
