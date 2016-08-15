from django.conf.urls import url
from . import views


app_name = "tasks"

urlpatterns = [
    url(r'^index$', views.index, name="index"),
    url(r'^$', views.example, name="example")
]
