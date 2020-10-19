# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand, CommandError
from vh_medproc.models import MedProc
from pyexcel_xlsx import get_data as xlsx_get
import os


class Command(BaseCommand):
	help = 'Load Excel file. Import medproc records into table'
	def add_arguments(self, parser):
		parser.add_argument('xls_file', nargs='?', type=str, default='medprocs.xlsx')
		parser.add_argument('row_start', nargs='?', type=int, default=1)
	
	def handle(self, *args, **options):
		xls_file = options['xls_file']
		row_start = options['row_start']
		
		n = 0
		data = xlsx_get(xls_file)
			
		for r in data['Import']:
			n+=1
			if len(r) == 3:
				if '.' in r[0]:
					#logger.info('row: {}'.format(r[9]))
					self.stdout.write('row {}'.format(n))
					#m = re.search('.*event\/(.+?)\/change.*', r[9])

					try:
						mp=MedProc.objects.get(code=r[0])
					except MedProc.DoesNotExist:
						mp = None

					if mp:
						if r[2] > 0:
							mp.price_old = mp.price
							mp.price = r[2]
						if mp.title != r[1]:
							mp.title = r[1]
						mp.save()
					else:
						mp=MedProc(code=r[0], title=r[1], title_check=r[1], price=r[2])
						mp.save()
							
		self.stdout.write(self.style.SUCCESS('Successfully import %d rows' % (n)))
