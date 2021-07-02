from django.urls import path
from.views import *



urlpatterns = [
    path('', index, name='index'),
    path('1', index1, name='index1'),
    # path('2', index2),
    # path('3', index3),
    # path('4', index4),
    # path('5', index5)
]