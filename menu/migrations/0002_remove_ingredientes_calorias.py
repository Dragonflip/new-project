# Generated by Django 4.1.7 on 2023-03-13 17:53

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("menu", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="ingredientes",
            name="calorias",
        ),
    ]
