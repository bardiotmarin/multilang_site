# Generated by Django 5.0.6 on 2024-06-27 03:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='stock_image_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
