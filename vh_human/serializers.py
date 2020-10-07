from django.contrib.auth.models import User
from .models import Human
from rest_framework import serializers

# class UserSerializer(serializers.ModelSerializer):
# 	class Meta:
# 		model = User
# 		fields = [ 'username']

class HumanSerializer(serializers.ModelSerializer):
	#usr = UserSerializer()
	class Meta:
		model = Human
		fields = ['uid', 'lastName', 'firstName', 'title', 'phone']

