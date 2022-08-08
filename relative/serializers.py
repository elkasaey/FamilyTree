from rest_framework import serializers
from .models import *

class RelativeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Relative
        fields = '__all__'


class GetRelativeSerializer(serializers.ModelSerializer):
    parents = GetRelativeSerializer(many = True)
    children = GetRelativeSerializer(many = True)
    class Meta:
        model = Relative
        fields = '__all__'
