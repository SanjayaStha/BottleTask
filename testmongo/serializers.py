from rest_framework import serializers
from .models import Cars, Name


class CarsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cars
        # fields = ['date']
        fields = '__all__'


class ClassifiedSerializer(serializers.ModelSerializer):

    from_date = serializers.DateField()
    to_date = serializers.DateField()
    count = serializers.IntegerField()
    emails = serializers.ListField()

    class Meta:
        model = Cars
        fields = [
            'from_date',
            'to_date',
            'count',
            'emails'
        ]


class NameSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cars
        fields = ('car_type',)
