# Generated by Django 4.1.7 on 2023-04-25 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0019_alter_order_order_book_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='order_item_ids',
        ),
        migrations.AlterField(
            model_name='salesrepresentative',
            name='mylab_id',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
