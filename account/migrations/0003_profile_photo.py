# Generated by Django 4.1.7 on 2023-02-26 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_rename_user_name_user_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='photo',
            field=models.ImageField(blank=True, upload_to='profile'),
        ),
    ]
