from django.urls import path
from PUPG import views


urlpatterns = [
    path("", views.index, name="index"),
    path("pets/", views.petsview.as_view(), name="pets"),
    path("submit/", views.submit, name="submit"),
    path("leaderboard/", views.leaderboard, name="leaderboard"),
    path("vote/", views.vote, name="vote")
]



#if settings.DEBUG:
#urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
