# Generated by Django 4.0 on 2022-01-28 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animal_husbandary', '0017_alter_vaccine_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='price',
            field=models.IntegerField(max_length=10),
        ),
    ]
