from django.urls import path
from .views import *

urlpatterns = [
    path("nearby/", GoogleMapsAPIView.as_view(), name="return nearby restaurants")
]
