# Generated by Django 4.2.3 on 2024-06-05 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supplier', '0002_order_supplierid_product_supplierid'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='productname',
            field=models.CharField(db_column='product_name', default='', max_length=99),
            preserve_default=False,
        ),
    ]
