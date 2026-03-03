from django.urls import path
from links import views

app_name = "links"
urlpatterns = [
    path("", views.index, name="index" )
]
