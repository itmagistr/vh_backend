#utils.py
from .settings import *
import json
import uuid
import requests
import time
import datetime
# import base64
import string
# from Crypto.Hash import SHA256
# from Crypto.PublicKey import RSA
# from Crypto.Signature import pkcs1_15
from django.utils import timezone
# from .models import CALENDAR_NAME_CHOICES
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)


def create_rbk_invoice(amount, product, desc, wishes):
	url = INV_URL
	uuidstr = '{}'.format(uuid.uuid1())
	dueDate = '{}'.format((timezone.now() + datetime.timedelta(days=1)).isoformat())

	headers = {
		"Content-type": "application/json; charset=utf-8",
		"X-Request-ID": uuidstr.replace('-',''),
		"X-Request-Deadline": "3s",
		"Authorization": "Bearer {}".format(PKEY),
		"Accept": "application/json"
		}
	shopID = SHOP_ID
	ddict = {
		'shopID': shopID,
		'dueDate': dueDate, 
		'amount': int(amount),
		'currency': 'RUB',
		'product': product,
		'description': desc,
		#'cart': [{'price': amount, 'product': product, 'quantity': 1, 'taxMode': {'type': 'InvoiceLineTaxVAT', 'rate': '18%'}}, ],
		'metadata': {'order_wishes': wishes}
		}
	#logger.info(f'ddict data: {ddict}')
	data = json.dumps(ddict, ensure_ascii=False).encode('utf-8')

	logger.info('HEADERS data: %s', headers)
	logger.info(f'POST data: {data}')
	token = ''
	iid = 0
	istatus = ''
	
	r = requests.post(url, headers=headers, data=data)
	logger.info('create_rbk_invoice response code: %s, %s', r.status_code, r.content)
	
	
	if r.status_code == 201:
		d = r.json()
		token = d["invoiceAccessToken"]["payload"]
		iid = d["invoice"]["id"]
		istatus = d["invoice"]["status"]
		#logger.info('response invoice token: %s', token)
		# logger.info('response invoice: %s, %s', iid, istatus)
	invoice = {'uuidstr': uuidstr, 'iid': iid, 'istatus': istatus, 'dueDate': dueDate, 'token': token}
	return {'code': r.status_code, 'invoice': invoice, 'content': r.content}