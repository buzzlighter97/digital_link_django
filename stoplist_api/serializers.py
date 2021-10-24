from rest_framework import serializers
from .models import Found, Numbers


class NumbersSerializer(serializers.Serializer):
    number = serializers.CharField(max_length=15, required=True)

    class Meta:
        fields = '__all__'
        model = Numbers


class FoundSerializer(serializers.Serializer):
    found = serializers.IntegerField(required=True)

    class Meta:
        fields = '__all__'
        model = Found