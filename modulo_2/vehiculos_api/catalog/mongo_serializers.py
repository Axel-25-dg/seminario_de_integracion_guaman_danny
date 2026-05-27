from rest_framework import serializers

class ServiceTypeSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=120)
    description = serializers.CharField(required=False, allow_blank=True)
    base_price = serializers.FloatField(required=False)
    is_active = serializers.BooleanField(default=True)

class VehicleServiceSerializer(serializers.Serializer):
    vehiculo_id = serializers.IntegerField()
    service_type_id = serializers.CharField()
    date = serializers.DateField(required=False)
    kilometers = serializers.IntegerField(required=False)
    cost = serializers.FloatField(required=False)
    notes = serializers.CharField(required=False, allow_blank=True)
