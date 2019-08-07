# Generated by Django 2.2.4 on 2019-08-05 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cars',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255)),
                ('gender', models.CharField(max_length=6)),
                ('ip_address', models.GenericIPAddressField()),
                ('createdAt', models.TimeField()),
                ('country', models.CharField(max_length=255)),
                ('date', models.DateField()),
                ('car_type', models.CharField(max_length=255)),
                ('manufacture_date', models.CharField(max_length=255)),
                ('manufacturer', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Name',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
    ]
