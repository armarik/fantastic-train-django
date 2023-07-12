from django.urls import path
from supercats import views

urlpatterns = [
    path('', views.hello_cat, name='hello_cat'),
    path("<int:cat_id>/results/", views.results, name="results"),
    path("<int:cat_id>/vote/", views.vote, name="vote"),
]
