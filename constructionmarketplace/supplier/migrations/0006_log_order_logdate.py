# Generated by Django 4.2.3 on 2024-06-06 01:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supplier', '0005_log_order_supplierid'),
    ]

    operations = [
        migrations.AddField(
            model_name='log_order',
            name='logdate',
            field=models.DateField(db_column='log_date', default='2024-01-01'),
            preserve_default=False,
        ),
    ]
