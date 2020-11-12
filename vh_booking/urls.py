#urls.py
from django.urls import include, path, re_path
from vh_booking import views


urlpatterns = [
    re_path('booking/create$', views.BookingCreateView.as_view()),
    re_path('booking/(?P<uid>[0-9a-f-]+)/$', views.BookingView.as_view()),
    re_path('booking/list/$', views.BookingFilterView.as_view()),
    
    
]