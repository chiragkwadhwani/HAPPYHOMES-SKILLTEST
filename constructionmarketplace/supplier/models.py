from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

class users(AbstractUser):
    id = models.AutoField(primary_key=True)
    password = models.CharField(max_length=255)
    last_login = models.CharField(max_length=50, blank=True)
    is_superuser = models.BooleanField(default=False)
    username = models.CharField(max_length=50, unique=True, error_messages={"unique":"This Username Already Exists"})
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, blank=True)
    email = models.EmailField(max_length=255, unique=True, error_messages={"unique":"This Email Already Exists"})
    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now, blank=True)
    date_modified = models.DateTimeField(default=timezone.now, blank=True)
    #custom new fields
    group = models.CharField(db_column='group', max_length=10,blank=True)
    biz_name = models.CharField(db_column='business_name', max_length=50)
    biz_info = models.CharField(db_column="business_description", max_length=99)
    biz_addr = models.CharField(db_column='business_address', max_length=99)
    biz_phone = models.CharField(db_column='business_number', max_length=15, unique=True, error_messages={"unique":"This Number Already Exists"})

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['username','first_name','biz_phone',]

    def __str__(self):
        return self.email
    
    class Meta:
        db_table = 'users'
        app_label = 'supplier'


class product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(db_column="item_name", max_length=99)
    desc = models.CharField(db_column="item_description", max_length=99)
    price = models.DecimalField(db_column="item_price", max_digits=19, decimal_places=2)
    availability = models.IntegerField(db_column="item_availability_count")
    supplierid = models.CharField(db_column="supplier_id", max_length=99)
    created = models.DateTimeField(db_column='created', auto_now_add=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'product'
        app_label = 'supplier'

class order(models.Model):
    id = models.AutoField(primary_key=True)
    orderid = models.IntegerField(db_column="order_id",blank=True,unique=True)
    productid = models.IntegerField(db_column="product_id",blank=True)
    buyerid = models.IntegerField(db_column="buyer_id",blank=True)
    supplierid = models.CharField(db_column="supplier_id", max_length=99,blank=True)
    productname = models.CharField(db_column="product_name", max_length=99)
    qty = models.IntegerField(db_column="quantity")
    totalprice = models.DecimalField(db_column="total_price", max_digits=19, decimal_places=2, blank=True)
    status = models.CharField(db_column="dispatch_status", max_length=99, blank=True)
    created = models.DateTimeField(db_column='created', auto_now_add=True)

    def __str__(self):
        return str(self.orderid)
    
    class Meta:
        db_table = 'orders'
        app_label = 'supplier'

class log_order(models.Model):
    id = models.AutoField(primary_key=True)
    orderid = models.IntegerField(db_column="order_id")
    supplierid = models.CharField(db_column="supplier_id", max_length=99)
    status = models.CharField(db_column="order_status", max_length=99)
    created = models.DateTimeField(db_column='created', auto_now_add=True)

    def __str__(self):
        return str(self.id)
    
    class Meta:
        db_table = 'log_order'
        app_label = 'supplier'

class review(models.Model):
    id = models.AutoField(primary_key=True)
    orderid = models.IntegerField(db_column="order_id")
    buyerid = models.IntegerField("buyer_id")
    description = models.CharField(db_column="description", max_length=99)
    rating = models.IntegerField(db_column="rating")
    created = models.DateTimeField(db_column='created', auto_now_add=True)

    def __str__(self):
        return self.description
    
    class Meta:
        db_table = 'review'
        app_label = 'supplier'