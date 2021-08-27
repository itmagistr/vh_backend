# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand, CommandError
from vh_product.models import *


class Command(BaseCommand):
	help = 'Truncate fields title_check, title_check_ru'
	def add_arguments(self, parser):
		parser.add_argument('max_len', nargs='?', type=int, default=100)
	
	def handle(self, *args, **options):
		max_len = options['max_len']
		prods = Product.objects.all()
		n = 0
		for prod in prods:
			self.stdout.write('{}, {} - starts truncate field'.format(prod.id, len(prod.title_check)))
			if len(prod.title_check) > max_len:
				prod.description = prod.title_check
				prod.description_ru = prod.title_check_ru
				prod.title_check = prod.title_check[:max_len]
				prod.title_check_ru = prod.title_check_ru[:max_len]
				prod.save()
				self.stdout.write('{}, {} - Ok'.format(prod.id, len(prod.title_check)))
				n+=1
		self.stdout.write(self.style.SUCCESS('Successfully truncated %d records' % (n)))
