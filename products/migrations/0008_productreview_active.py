# Generated by Django 3.1.2 on 2021-01-26 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_productreview'),
    ]

    operations = [
        migrations.AddField(
            model_name='productreview',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
