# Generated by Django 4.2.2 on 2023-07-19 09:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_company_remove_profile_max_storage_and_more'),
        ('backups', '0004_remove_backup_filesize_str'),
    ]

    operations = [
        migrations.AddField(
            model_name='backup',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.company'),
        ),
    ]
