from django.urls import path
from . import views

app_name = "home"

urlpatterns = [
    path("contact/", views.contact, name="contact"),
    path("", views.home_view, name="homepage"),

]