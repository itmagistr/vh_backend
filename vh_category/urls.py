#urls.py
from django.urls import include, path, re_path
from vh_category import views

urlpatterns = [
	re_path('category/$', views.CategoryListView.as_view()),
	#re_path('category/(?P<uid>[0-9a-f-]+)/$', views.CategoryView.as_view()),
	#re_path('category/list/$', views.CategoryFilterView.as_view()),
	# re_path('category/spec/list/$', views.ListView.as_view()),

]