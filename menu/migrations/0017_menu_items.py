# Generated by Django 4.1.7 on 2023-03-17 14:58

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("menu", "0016_menumedia"),
    ]

    operations = [
        migrations.AddField(
            model_name="menu",
            name="items",
            field=models.ManyToManyField(blank=True, to="menu.item"),
        ),
    ]