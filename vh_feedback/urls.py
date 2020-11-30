# urls.py
from django.urls import include, path, re_path
from vh_feedback import views

urlpatterns = [
	re_path('feedback/(?P<uid>[0-9a-f-]+)/$', views.FeedbackView.as_view()),
	re_path('feedback/call/$', views.FeedbackCallCreateView.as_view()),
	re_path('feedback/msg/$', views.FeedbackCreateView.as_view()),

]