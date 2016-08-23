from rest_framework import serializers
from .models import Ability


class AbilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Ability
        fields = ('id', 'name', 'description', 'power_level')
