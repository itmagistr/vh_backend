from .models import Doctor, Special
from rest_framework import serializers
from vh_human.serializers import HumanSerializer



class SpecialSerializer(serializers.ModelSerializer):
	class Meta:
		model = Special
		fields = [ 'title']

class DoctorSerializer(serializers.ModelSerializer):#serializers.HyperlinkedModelSerializer):
	human = HumanSerializer()
	special = SpecialSerializer()
	class Meta:
		model = Doctor
		fields = ['human', 'special', 'youtube']
		#fields = ['uid', 'lastName', 'firstName', 'title', 'phone', 'special']

