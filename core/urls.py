from django.urls import path
from .import views

urlpatterns = [
    path("", views.index, name="index"),
    #ex: /deuda/5/
    path("<int:id>/", views.detail, name="details"),
    path("<int:id>/results/", views.reult, name="results"),
    path("<int:id>/vote/", views.index, name="vote"),
    
]
