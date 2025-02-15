# Generated by Django 4.1.7 on 2023-05-13 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_alter_distributor_appointed_by_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='salesrepresentative',
            name='email',
        ),
        migrations.AlterField(
            model_name='salesrepresentative',
            name='designation',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='salesrepresentative',
            name='joining_data',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='salesrepresentative',
            name='location_coverage',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
