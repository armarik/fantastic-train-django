from django.urls import path
from supercats import views

urlpatterns = [
    path('', views.hello_cat, name='hello_cat'),
]
