# Generated by Django 4.0 on 2022-01-12 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animal_husbandary', '0008_vaccine_animal'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vaccine',
            name='animal',
        ),
        migrations.AddField(
            model_name='vaccine',
            name='anim',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
