from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from rbkpay.models import RBKInvoice
from vh_medproc.models import MedProc
# from vh_client.models import Client

# from .models import Invoice
from drf_yasg.utils import swagger_auto_schema
# from drf_yasg import openapi
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)

class InvoiceCreateView(generics.CreateAPIView):
	'''
	Создание счета для оплаты брони записи
	'''
	serializer_class = InvoiceOutSerializer
	http_method_names = ['post']
	@swagger_auto_schema(request_body=InvoiceInSerializer, responses={200: InvoiceOutSerializer, 409: InvoiceOutErrorSerializer})
	def post(self, request, *args, **kwargs):
		serializer = InvoiceInSerializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		# sclass = self.get_serializer_class()

		mp = MedProc.objects.get(uid=serializer.data['medproc_uid'])
		# cl = Client.objects.get(uid=serializer.data['client_uid'])

		#https://developer.rbk.money/api/#operation/createInvoice
		try:
			inv = RBKInvoice.create(price=mp.price, title=mp.title_check_ru, desc=mp.description_ru, wishes='тестовый счет')
			resSerializer = InvoiceOutSerializer({
								
								'invoice_id' : inv.iid,
								'invoice_expire' : inv.expire,
								'invoice_token' : inv.token,
								'invoice_status' : inv.status,
								'invoice_title' : inv.title,
								'invoice_email' : 'email_test@mail.ru',
								'invoice_desc' : inv.descr
								})
		except:
			logger.info('Error response code %s to create invoice data', '')
			resSerializer = InvoiceOutErrorSerializer({'response_code' : 409,
														'message' : 'ERROR',
													})
			return Response(resSerializer.data, status=status.HTTP_409_CONFLICT)
		return Response(resSerializer.data, status=status.HTTP_200_OK)