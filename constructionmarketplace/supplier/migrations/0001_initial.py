# Generated by Django 4.2.3 on 2024-06-05 15:07

import django.contrib.auth.models
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='log_order',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('orderid', models.IntegerField(verbose_name='order_id')),
                ('status', models.CharField(db_column='order_status', max_length=99)),
                ('created', models.DateTimeField(auto_now_add=True, db_column='created')),
            ],
            options={
                'db_table': 'log_order',
            },
        ),
        migrations.CreateModel(
            name='order',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('orderid', models.IntegerField(db_column='order_id')),
                ('productid', models.IntegerField(db_column='product_id')),
                ('buyerid', models.IntegerField(db_column='buyer_id')),
                ('qty', models.IntegerField(db_column='quantity')),
                ('totalprice', models.DecimalField(db_column='total_price', decimal_places=2, max_digits=19)),
                ('status', models.CharField(db_column='dispatch_status', max_length=99)),
                ('created', models.DateTimeField(auto_now_add=True, db_column='created')),
            ],
            options={
                'db_table': 'order',
            },
        ),
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='item_name', max_length=99)),
                ('desc', models.CharField(db_column='item_description', max_length=99)),
                ('price', models.DecimalField(db_column='item_price', decimal_places=2, max_digits=19)),
                ('availability', models.IntegerField(db_column='item_availability_count')),
                ('created', models.DateTimeField(auto_now_add=True, db_column='created')),
            ],
            options={
                'db_table': 'product',
            },
        ),
        migrations.CreateModel(
            name='review',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('buyerid', models.IntegerField(verbose_name='buyer_id')),
                ('description', models.CharField(db_column='description', max_length=99)),
                ('rating', models.IntegerField(db_column='rating')),
                ('created', models.DateTimeField(auto_now_add=True, db_column='created')),
            ],
            options={
                'db_table': 'review',
            },
        ),
        migrations.CreateModel(
            name='users',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=255)),
                ('last_login', models.CharField(blank=True, max_length=50)),
                ('is_superuser', models.BooleanField(default=False)),
                ('username', models.CharField(error_messages={'unique': 'This Username Already Exists'}, max_length=50, unique=True)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(blank=True, max_length=50)),
                ('email', models.EmailField(error_messages={'unique': 'This Email Already Exists'}, max_length=255, unique=True)),
                ('is_staff', models.BooleanField(default=True)),
                ('is_active', models.BooleanField(default=True)),
                ('date_joined', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
                ('date_modified', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
                ('propcode', models.CharField(blank=True, db_column='property_code', max_length=10)),
                ('group', models.CharField(db_column='group', max_length=10)),
                ('biz_name', models.CharField(db_column='business_name', max_length=50)),
                ('biz_info', models.CharField(db_column='business_description', max_length=99)),
                ('biz_addr', models.CharField(db_column='business_address', max_length=99)),
                ('biz_phone', models.CharField(db_column='business_number', error_messages={'unique': 'This Number Already Exists'}, max_length=15, unique=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'db_table': 'users',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
