#urls.py
from django.urls import include, path, re_path
from vh_medproc import views


urlpatterns = [
    re_path('medproc/$', views.MedProcListView.as_view()),
    re_path('medproc/(?P<uid>[0-9a-f-]+)/$', views.MedProcView.as_view()),
    re_path('medproc/(?P<uid>[0-9a-f-]+)/doctors/$', views.MedProcDoctorsView.as_view()),
    re_path('medproc/(?P<uid>[0-9a-f-]+)/light/$', views.MedProcLightView.as_view()),
    re_path('medproc/list/$', views.MedProcFilterView.as_view()),
    re_path('mpfiltered/$', views.MedProcFilterView1.as_view()),
    re_path('mpsearch/$', views.MedProcSearchView.as_view())
    
]