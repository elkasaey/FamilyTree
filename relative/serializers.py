from rest_framework import serializers
from .models import *

class RelativeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Relative
        fields = '__all__'

    def validate(self, data):
        for parent in data['parents']:
            if parent.birthdate > data['birthdate']:
                raise serializer.ValidationError(
                    'You cannot be older than you parent {parent}!'.format(
                                                            parent=parent))
        return data
