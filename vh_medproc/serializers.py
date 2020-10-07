from .models import MedProc
from rest_framework import serializers
from vh_product.serializers import *

class MedProcSerializer(serializers.HyperlinkedModelSerializer):
	uid = serializers.CharField(source='product.uid')
	title = serializers.CharField(source='product.title')
	title_check = serializers.CharField(source='product.title_check')
	price = serializers.DecimalField(source='product.price', max_digits=10, decimal_places=2)
	price_old = serializers.DecimalField(source='product.price_old', max_digits=10, decimal_places=2)
	description = serializers.CharField(source='product.description')
	#product = ProductSerializer()
	class Meta:
		model = MedProc
		fields = ['uid', 'title', 'title_check', 'price', 'price_old', 'duration', 'description']

