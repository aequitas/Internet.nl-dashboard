# Generated by Django 2.2.2 on 2019-06-24 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('internet_nl_dashboard', '0034_auto_20190613_0946'),
    ]

    operations = [
        migrations.AlterField(
            model_name='urllist',
            name='last_manual_scan',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
