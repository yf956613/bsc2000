# -*- coding:utf-8 -*-
from django.conf.urls import url
from django.contrib import admin

from .views import (
    BigmeterCreateAPIView,
    flowdata_dailyuse,
    datatalbe_test,
    TempTestListAPIView,
)

app_name='amrs-api'
urlpatterns = [
    
    url(r'^bigmeter/create/$', BigmeterCreateAPIView.as_view(), name='bigmeter-create'),

    url(r'^flowdata_dailyuse/$', flowdata_dailyuse, name='flowdata_dailyuse'),
    # datatable test
    url(r'^datatable/test/$', TempTestListAPIView.as_view(), name='datatalbe_test'),

]
