from rest_framework import serializers


class apiSerializer(serializers.Serializer):
    amount = serializers.IntegerField()
    numberPlate = serializers.CharField(max_length=50)
