from django.urls import path
from . import views

urlpatterns = [
    path("bot-response", views.sendResponse, name="bot-says")
]