# Generated by Django 4.1.7 on 2023-03-13 20:53

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("menu", "0006_alter_item_item_media_id"),
    ]

    operations = [
        migrations.AddField(
            model_name="item",
            name="ingredientes",
            field=models.ManyToManyField(null=True, to="menu.ingredientes"),
        ),
    ]
