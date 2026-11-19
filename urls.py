from django.urls import path
from django.views.generic import TemplateView
from .api import Dlist, Dhtviews

urlpatterns = [
    path("list/", Dlist, name="dht-list"),
    path("post/", Dhtviews.as_view(), name="dht-create"),
    path("dashboard/", TemplateView.as_view(template_name="DHT/dashboard.html"), name="dashboard"),
]