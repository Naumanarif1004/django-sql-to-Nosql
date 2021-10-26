from django.urls import path
from .views import *
from django.conf.urls import url
urlpatterns = [

    url('', ConvertTableDataToJsonApi.as_view(), name='countries-list'),
]
