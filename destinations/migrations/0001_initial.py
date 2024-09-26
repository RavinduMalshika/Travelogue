# Generated by Django 4.2.12 on 2024-09-26 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Destination',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='pics')),
                ('destination_type', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=200)),
                ('rating', models.FloatField(default=0.0)),
            ],
        ),
    ]
