# Generated by Django 4.2.3 on 2024-06-06 02:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('supplier', '0006_log_order_logdate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='log_order',
            name='logdate',
        ),
    ]