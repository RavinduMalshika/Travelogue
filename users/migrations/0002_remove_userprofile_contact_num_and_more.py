# Generated by Django 4.2.12 on 2024-10-02 14:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='contact_num',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='country',
        ),
    ]
