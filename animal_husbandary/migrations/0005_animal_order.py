# Generated by Django 4.0 on 2022-01-11 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animal_husbandary', '0004_remove_purchase_ord'),
    ]

    operations = [
        migrations.AddField(
            model_name='animal',
            name='order',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
