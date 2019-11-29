from django.urls import path, include
from django.conf.urls import url
from robokassa.views import receive_result, success, fail


urlpatterns = [
    path('result/', receive_result, name="robokassa_result"),
    path('success/', success, name="robokassa_success"),
    path('fail/', fail, name="robokassa_fail"),
]
