# Generated by Django 4.0 on 2022-01-27 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animal_husbandary', '0015_alter_customer_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='vaccine',
            name='vaccinated',
            field=models.ManyToManyField(to='animal_husbandary.animal'),
        ),
        migrations.DeleteModel(
            name='vaccinated',
        ),
    ]
