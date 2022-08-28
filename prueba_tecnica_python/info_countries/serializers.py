import hashlib
from typing_extensions import Required
from rest_framework import serializers
from .models import *

class CountrySerializer(serializers.ModelSerializer):
	class Meta:
		model = Country
		fields = "__all__"

class LanguageCountrySerializer(serializers.ModelSerializer):
	class Meta:
		model = LanguageCountry
		fields = "__all__"
	
	def create(self, validated_data):
		languageSha1 = hashlib.sha1(str(validated_data.get('language')).encode('utf-8'))
		instance = LanguageCountry.objects.create(**validated_data)
		instance.set_language(languageSha1.hexdigest())
		instance.save()
		return instance
