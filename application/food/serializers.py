from django.contrib.auth.models import User, Group
from rest_framework import serializers
from food.models import *

# class FoodSerializer(serializers.Serializer):
# 	pk = serializers.IntegerField(read_only=True)
# 	title = serializers.CharField(required=True, max_length=500)

# 	def create(self, validated_data):
# 		return Food.objects.create(**validated_data)

# 	def update(self, instance, validated_data):
# 		instance.title = validated_data.get('title', instance.title)
# 		instance.save()
# 		return instance


class FoodSerializer(serializers.ModelSerializer):
	class Meta:
		model = Food
		# fields = ('id', 'title','ingridients')