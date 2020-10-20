from django.urls import include, path, re_path
from rest_framework import routers
from django.views.generic import TemplateView
from rest_framework.schemas import get_schema_view
from . import views

router = routers.DefaultRouter()
# router.register(r'users', views.UserViewSet, basename='user')
# router.register(r'groups', views.GroupViewSet, basename='group')
router.register(r'medproc', views.MedProcViewSet, basename='medproc')
router.register(r'doctor', views.DoctorViewSet, basename='doctor')


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

apipatterns = [
	path('', include(router.urls)),
	re_path('daystatus/(?P<dstart>\d\d\d\d-\d\d-\d\d)/(?P<dend>\d\d\d\d-\d\d-\d\d)/$', views.DayStatusView.as_view()),
	re_path('timetatus/(?P<d>\d\d\d\d-\d\d-\d\d)/$', views.TimeStatusView.as_view()),
	re_path('mpfiltered/$', views.MedProcFilterView.as_view())
]
urlpatterns = []
urlpatterns += apipatterns

urlpatterns +=[
		
	path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
	
	path('openapi', get_schema_view(
						title='vHollyWood API',
						url='/vhapi/',
						patterns=apipatterns,
					), name='openapi-schema'),

	path('swagger-ui/', TemplateView.as_view(
		 template_name='swager-ui.html',
		 extra_context={'schema_url':'openapi-schema'} ), name='swagger-ui'),
]