# Generated by Django 4.2.3 on 2024-06-06 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supplier', '0010_alter_product_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(db_column='item_name', error_messages={'unique': 'This Item Already Exists'}, max_length=99, unique=True),
        ),
    ]
