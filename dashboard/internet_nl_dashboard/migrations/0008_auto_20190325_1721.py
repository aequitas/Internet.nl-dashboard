# Generated by Django 2.1.7 on 2019-03-25 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('internet_nl_dashboard', '0007_remove_account_enable_logins'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='enable_scans',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='urllist',
            name='enable_scans',
            field=models.BooleanField(default=True),
        ),
    ]
