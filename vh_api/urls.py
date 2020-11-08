from django.urls import include, path, re_path
from rest_framework import routers
from django.views.generic import TemplateView
#from rest_framework.schemas import get_schema_view
from drf_yasg.views import get_schema_view
from drf_yasg.generators import OpenAPISchemaGenerator
from drf_yasg import openapi
from . import views
import os

#router = routers.DefaultRouter()
# router.register(r'users', views.UserViewSet, basename='user')
# router.register(r'groups', views.GroupViewSet, basename='group')
#router.register(r'medproc', views.MedProcViewSet, basename='medproc')
# router.register(r'doctor', views.DoctorViewSet, basename='doctor')


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

class SchemaGenerator(OpenAPISchemaGenerator):
  def get_schema(self, request=None, public=False):
    schema = super(SchemaGenerator, self).get_schema(request, public)
    schema.basePath = os.path.join(schema.basePath, 'ru/vhapi/')
    return schema

apipatterns = [
	#path('', include(router.urls)),
	re_path('daystatus/(?P<dstart>\d\d\d\d-\d\d-\d\d)/(?P<dend>\d\d\d\d-\d\d-\d\d)/$', views.DayStatusView.as_view()),
	re_path('timestatus/(?P<d>\d\d\d\d-\d\d-\d\d)/$', views.TimeStatusView.as_view()),
	path('', include('vh_doctor.urls')),
	path('', include('vh_medproc.urls')),
	path('', include('vh_booking.urls')),
	re_path('timeslot/day/$', views.TimeSlotDayView.as_view()),
	re_path('timeslot/day/list$', views.TimeSlotDayListView.as_view()),
	re_path('timeslot/list/$', views.TimeSlotListView.as_view()),
	]
urlpatterns = []
urlpatterns += apipatterns



schema_view = get_schema_view(info=openapi.Info(title='vHollyWood API', default_version='v0.1'),
				url='http://localhost:8000/',
				patterns=apipatterns,
				public=False, 
				urlconf="management_server.api.urls",
				generator_class=SchemaGenerator,)

urlpatterns +=[
		
	path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
	path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

	# path('openapi', get_schema_view(
	# 					title='vHollyWood API',
	# 					url='/vhapi/',
	# 					patterns=apipatterns,
	# 				), name='openapi-schema'),

	# path('swagger-ui/', TemplateView.as_view(
	# 	 template_name='swager-ui.html',
	# 	 extra_context={'schema_url':'openapi-schema'} ), name='swagger-ui'),
]