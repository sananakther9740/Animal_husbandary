# Generated by Django 4.0 on 2022-01-09 17:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='customer',
            fields=[
                ('customerID', models.AutoField(primary_key=True, serialize=False)),
                ('CustomerName', models.CharField(max_length=30)),
                ('phoneNo', models.BigIntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=45)),
                ('Address', models.CharField(max_length=45)),
                ('city', models.CharField(max_length=45)),
                ('state', models.CharField(max_length=45)),
                ('pincode', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cname', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('suggestion', models.TextField()),
                ('improvements', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='food',
            fields=[
                ('foodID', models.IntegerField(primary_key=True, serialize=False)),
                ('datetime', models.DateTimeField()),
                ('quantity', models.IntegerField()),
                ('fooditem', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='staff',
            fields=[
                ('staffID', models.IntegerField(primary_key=True, serialize=False)),
                ('staffName', models.CharField(max_length=30)),
                ('Address', models.TextField()),
                ('phone', models.BigIntegerField()),
                ('designation', models.CharField(max_length=30)),
                ('dateofjoin', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='staflog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='vaccine',
            fields=[
                ('vaccineID', models.IntegerField(primary_key=True, serialize=False)),
                ('remark', models.CharField(max_length=30)),
                ('date_of_vaccination', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='animal',
            fields=[
                ('animalID', models.IntegerField(primary_key=True, serialize=False)),
                ('typeofanimal', models.CharField(max_length=30)),
                ('gender', models.CharField(max_length=30)),
                ('price', models.CharField(max_length=10)),
                ('status', models.CharField(max_length=30)),
                ('stf', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='animal_husbandary.staff')),
            ],
        ),
        migrations.CreateModel(
            name='vaccinated',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anim', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='animal_husbandary.animal')),
                ('vaccn', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='animal_husbandary.vaccine')),
            ],
            options={
                'unique_together': {('anim', 'vaccn')},
            },
        ),
        migrations.CreateModel(
            name='purchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('amount', models.IntegerField()),
                ('anim', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='animal_husbandary.animal')),
                ('cust', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='animal_husbandary.customer')),
            ],
            options={
                'unique_together': {('cust', 'anim')},
            },
        ),
        migrations.CreateModel(
            name='eats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anim', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='animal_husbandary.animal')),
                ('fd', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='animal_husbandary.food')),
            ],
            options={
                'unique_together': {('anim', 'fd')},
            },
        ),
    ]