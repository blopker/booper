# Generated by Django 5.0.1 on 2024-02-08 03:39

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("booperapp1", "0002_auto_20240201_0530"),
    ]

    operations = [
        migrations.AddField(
            model_name="boop",
            name="thisID",
            field=models.IntegerField(default=0),
        ),
    ]
