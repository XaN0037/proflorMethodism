from django.urls import path

from dashboard.views import Main

urlpatterns = [

    path("", Main.as_view())

              ]
