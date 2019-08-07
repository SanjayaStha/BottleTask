from django.urls import path, include
from rest_framework import routers
from .views import CarsDetailView, NameView, ClassifiedView

routers = routers.DefaultRouter()

routers.register(r'detail', CarsDetailView),
routers.register(r'classified', ClassifiedView, base_name='classified'),
routers.register(r'name', NameView, base_name='name')

urlpatterns = routers.urls


