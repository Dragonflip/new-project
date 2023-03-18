# Generated by Django 4.1.7 on 2023-03-17 14:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("menu", "0012_alter_item_ingredientes"),
    ]

    operations = [
        migrations.AlterField(
            model_name="item",
            name="ingredientes",
            field=models.ManyToManyField(blank=True, to="menu.ingredientes"),
        ),
        migrations.AlterField(
            model_name="menu",
            name="categoria",
            field=models.ForeignKey(
                blank=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="menu.menucategoria",
            ),
        ),
    ]
