# Generated by Django 2.2.1 on 2019-05-28 13:52

from django.db import migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('internet_nl_dashboard', '0031_account_report_settings'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='report_settings',
            field=jsonfield.fields.JSONField(blank=True, help_text='This stores reporting preferences: what fields are shown in the UI and so on (if any other).This field can be edited on the report page.', null=True),
        ),
    ]
