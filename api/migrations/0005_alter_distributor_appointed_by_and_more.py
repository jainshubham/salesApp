# Generated by Django 4.1.7 on 2023-05-11 13:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_salesrepresentative_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='distributor',
            name='appointed_by',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='distributor',
            name='category',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='distributor',
            name='head_quarter',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='distributor',
            name='sales_rep',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.salesrepresentative'),
        ),
        migrations.AlterField(
            model_name='distributor',
            name='state',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
