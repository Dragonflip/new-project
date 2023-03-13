# Generated by Django 4.1.7 on 2023-03-13 20:17

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("menu", "0003_itemmedia_item"),
    ]

    operations = [
        migrations.AddField(
            model_name="itemmedia",
            name="title",
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AlterField(
            model_name="itemmedia",
            name="imagem",
            field=models.ImageField(upload_to="items"),
        ),
    ]
