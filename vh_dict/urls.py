#urls.py
from django.urls import include, path, re_path
from vh_dict import views


urlpatterns = [
    re_path('dictstr/$', views.DictStrListView.as_view()),
    re_path('dictstr/list/$', views.DictStrFilterView.as_view()),
]