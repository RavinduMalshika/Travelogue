# Generated by Django 5.1.1 on 2024-10-04 03:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_remove_userprofile_contact_num_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='profile_picture',
            field=models.ImageField(default=1, upload_to='pics'),
            preserve_default=False,
        ),
    ]
