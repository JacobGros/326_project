from django.urls import path
from PUPG import views


urlpatterns = [
    path("", views.index, name="index"),
    #path("pets/", views.petsview, name="pets"),
]
