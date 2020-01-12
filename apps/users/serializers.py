from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):

	class Meta:
		model = User
		fields = ['username', 'first_name', 'last_name', 'email', 'is_staff', 'password', 'id']
		extra_kwargs = {
			'password': { 'write_only': True }
		}

	def create(self, validated_data):
		user = User(
			username=validated_data['username'],
			email=validated_data['email'],
			first_name=validated_data['first_name'],
			last_name=validated_data['last_name'],
			is_staff=validated_data['is_staff']
		)
		user.set_password(validated_data['password'])
		user.save()
		return user