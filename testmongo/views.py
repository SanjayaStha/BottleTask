from django.db.models import Count
from rest_framework import viewsets
from .models import Cars, Name
from .serializers import CarsSerializer, NameSerializer, ClassifiedSerializer
import datetime
from django.utils import timezone


class CarsDetailView(viewsets.ModelViewSet):
    queryset = Cars.objects.all()
    serializer_class = CarsSerializer


class ClassifiedView(viewsets.ModelViewSet):
    serializer_class = ClassifiedSerializer
    name = 'classified'

# """ Date field is updated in DB, from 01/18/2019 format to 2019-01-18 standard format of django"""

    def get_queryset(self):
        # print(len(Cars.objects.values('car_type')))
        start = Cars.objects.earliest('date').date # finding the earliest date in date column
        end = Cars.objects.latest('date').date # finding the latest date in date column

        datalist = []

        end_date = start
        while start < end: # looping from earliest date to latest date
            datadict = {}   # dict to store the data
            end_date = start + datetime.timedelta(days=10) # updating end date to classify within intervals,

            data = Cars.objects.filter(date__range=[start, end_date]) # fetching data in the range of 10 days
            count = len(data.values('car_type').distinct()) # counting no of cars

            # distinct = data.values(
            #     'car_type'
            # ).annotate(
            #     car_count=Count('car_type')
            # ).filter(car_count=1)
            # records = data.filter(car_type__in=[item['car_type'] for item in distinct])
            # print(records.count())
            # count = records.count()
            emails = data.values('email')
            em = []
            for email in emails:
                em.append(email['email'])

            datadict['from_date'] = start
            datadict['to_date'] = end_date
            datadict['count'] = count
            datadict['emails'] = em

            start = end_date + datetime.timedelta(days=1)

            if end_date > end:
                end_date = end
            datalist.append(datadict)

        sort_list = sorted(datalist, key = lambda i: i['count'])

        return sort_list


class NameView(viewsets.ModelViewSet):
    queryset = Cars.objects.values('car_type')
    serializer_class = NameSerializer
    name = 'name'


