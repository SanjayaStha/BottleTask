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

    def get_queryset(self):

        start = Cars.objects.earliest('date').date
        end = Cars.objects.latest('date').date

        datalist = []

        end_date = start
        while start < end:
            datadict = {}
            end_date = start + datetime.timedelta(days=10)
            print(start, 'start')
            print(end_date, 'end_date')
            data = Cars.objects.filter(date__range=[start, end_date])
            count = data.count()
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
    # queryset = Name.objects.all()
    # serializer_class = NameSerializer
    # name = 'name'
    pass

