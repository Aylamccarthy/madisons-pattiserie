# Generated by Django 3.2.21 on 2023-11-12 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_reviews', '0007_auto_20231111_2250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='date_created_on',
            field=models.DateTimeField(default='2023-11-12 13:35:13'),
        ),
        migrations.AlterField(
            model_name='review',
            name='date_updated_on',
            field=models.DateTimeField(default='2023-11-12 13:35:13'),
        ),
    ]
