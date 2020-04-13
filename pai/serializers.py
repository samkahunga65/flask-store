from .models import Covid, Region
from rest_framework import serializers


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = '__all__'


class CovidSerializer(serializers.ModelSerializer):
    region = RegionSerializer(many=False)
    periodType = serializers.CharField(max_length=120)
    timeToElapse = serializers.IntegerField(default=0)
    reportedCases = serializers.IntegerField(default=0)
    population = serializers.IntegerField(default=0)
    populatotalHospitalBedstion = serializers.IntegerField(default=0)
    totalHospitalBeds = serializers.IntegerField(default=0)

    def create(self, validated_data):
        return Covid.objects.create(**validated_data)

    class Meta:
        model = Covid
        fields = ['region', 'periodType', 'timeToElapse',
                  'reportedCases', 'populatotalHospitalBedstion', 'population', 'totalHospitalBeds']
