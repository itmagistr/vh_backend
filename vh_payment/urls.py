#urls.py
from django.urls import include, path, re_path
from vh_payment import views


urlpatterns = [

    re_path('invoice/create/$', views.InvoiceCreateView.as_view(), name='invoice-create'),
    
    
]