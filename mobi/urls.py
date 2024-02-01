from django.urls import path
from mobi.views import *
app_name = 'mobi'
urlpatterns = [
    path('',welcome,name='welcome'),
    path('index.htm', index, name='index'),
    path('predict/',predict, name='predict'),
     path('get_phone_details/', get_phone_details, name='get_phone_details'),
]