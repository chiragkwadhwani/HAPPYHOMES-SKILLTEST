from supplier.models import *
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = users
        exclude = ('password','last_login','is_superuser','propcode','is_staff','user_permissions',)
        labels = {'email':'','first_name':'', 'groups':'', 'first_name':'', 'last_name':'', 
                'is_active':'', 'username':'', 'mobilenum':'', 'password':'', 'password1':'', 'password2':'',
                'biz_name':'', 'biz_info':'', 'biz_addr':'','biz_phone':''}

class CustomUserChangeForm(UserChangeForm):
    def __init__(self, *args, **kwargs):
        super(CustomUserChangeForm, self).__init__(*args, **kwargs)

    class Meta:
        model = users
        fields = '__all__'
        labels = {'email':'','first_name':'', 'first_name':'', 'last_name':'', 'is_active':'', 'username':'', 
                'password':'', 'password1':'', 'password2':'', 'biz_name':'', 'biz_info':'', 'biz_addr':'','biz_phone':''}

class productform(forms.ModelForm):

    class Meta:
        model = product
        fields = '__all__'
        labels = {'name':'Product Name','desc':'Product Description','price':'Price of product','availability':'Stock Count'}

class orderform(forms.ModelForm):
    product_list = product.objects.all().order_by('name')
    productname = forms.ModelChoiceField(queryset=product_list,label="",to_field_name='id')

    class Meta:
        model = order
        exclude = {'status','totalprice','supplierid','orderid','buyerid','productid'}
        labels = {'orderid':'Order ID','productid':'Product ID','buyerid':'Buyer ID','supplierid':'Supplier ID',
                  'productname':'Product Name','qty':'Quantity','totalprice':'Total Price','status':'Status','created':'Created'}
