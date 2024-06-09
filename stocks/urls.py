from django.urls import path
from . import views
from .views import *

app_name = "stocks"

urlpatterns = [
    path("", views.index, name="index"),
    path("create/", StockCreateView.as_view(), name="create"),
]
