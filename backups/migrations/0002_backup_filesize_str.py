# Generated by Django 4.2 on 2023-05-19 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backups', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='backup',
            name='filesize_str',
            field=models.CharField(default='0 bytes', max_length=100),
        ),
    ]