from django.urls import path
from PUPG import views


urlpatterns = [
    path("", views.index, name="index"),
    path("pets/", views.petsview.as_view(), name="pets"),
    path("submit/", views.submit, name="submit"),
    path("leaderboard/", views.leaderboard, name="leaderboard"),
]
