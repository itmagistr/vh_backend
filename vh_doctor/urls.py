#urls.py
from django.urls import include, path, re_path
from vh_doctor import views

urlpatterns = [
	re_path('doctor/$', views.DoctorListView.as_view()),
	re_path('doctor/(?P<uid>[0-9a-f-]+)/$', views.DoctorView.as_view()),
	re_path('doctor/list/$', views.DoctorFilterView.as_view()),
	re_path('doctor/spec/list/$', views.SpecListView.as_view()),
	re_path('doctor/(?P<uid>[0-9a-f-]+)/workres/$', views.DocWorkResView.as_view()),

]