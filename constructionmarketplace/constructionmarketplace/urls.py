"""
URL configuration for constructionmarketplace project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from supplier import views

urlpatterns = [
    path('superadmin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', views.index, name='dashboard'),
    path('details/', views.supplierdetails, name='supplierpage'),
    path('suppliersignup/', views.suppliersignup, name='suppliersignup'),
    path('details/dispatched/<int:orderid>/', views.markasdispatched, name='markasdispatched'),
    path('details/processing/<int:orderid>/', views.markasbeingprocessed, name='markasbeingprocessed'),
    path('details/completed/<int:orderid>/', views.markascompleted, name='markascompleted'),
    path('details/products/<int:supplierid>/', views.productslist, name='productslist'),
    path('details/products/<str:case>/<int:supplierid>/<int:productid>/', views.productdetail, name='productdetail'),
    path('details/logs/<int:supplierid>/', views.displaylogs, name='logs'),
    path('details/statement/<int:supplierid>/', views.showrevenue, name='revenue'),
    path('details/createorder/<int:supplierid>/', views.createorder, name='createorder'),

    path('forbidden/', views.error_403, name='error_403_forbidden'),
    path('pagenotfound/', views.error_404, name='error_404_notfound'),
    path('methodnotallowed/', views.error_405, name='error_405_methodnotallowed'),
    path('internalservererror/', views.error_500, name='error_500_internalservererror'),
    path('notavailable_featurecomingsoon/', views.feature_coming_soon, name='featurecomingsoon'),
]

handler403 = views.err_403
handler404 = views.err_404
handler405 = views.err_405
handler500 = views.err_500
