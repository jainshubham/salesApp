# Generated by Django 4.1.7 on 2023-05-11 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_salesrepresentative_reporting_business_unit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salesrepresentative',
            name='gender',
            field=models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=100, null=True),
        ),
    ]
