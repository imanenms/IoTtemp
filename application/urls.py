from django.urls import path, include

from application import views

urlpatterns = [

    path('', views.dash,name="acc")
]