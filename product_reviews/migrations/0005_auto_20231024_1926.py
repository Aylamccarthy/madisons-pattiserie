# Generated by Django 3.2.21 on 2023-10-24 19:26

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("product_reviews", "0004_auto_20231023_2027"),
    ]

    operations = [
        migrations.AlterField(
            model_name="review",
            name="date_created_on",
            field=models.DateTimeField(default="2023-10-24 19:26:29"),
        ),
        migrations.AlterField(
            model_name="review",
            name="date_updated_on",
            field=models.DateTimeField(default="2023-10-24 19:26:29"),
        ),
    ]
