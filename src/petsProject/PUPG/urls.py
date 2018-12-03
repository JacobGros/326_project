from django.urls import path
from PUPG import views


urlpatterns = [
    path("", views.index, name="index"),
    path("submit/", views.PetCreateView.as_view(), name="submit"),
    path("leaderboard/", views.leaderboard, name="leaderboard"),
    path("vote/", views.vote, name="vote"),
    path('person/<int:pk>', views.PersonDetailView.as_view(), name='person-detail'),
    path('pet/<int:pk>', views.PetDetailView.as_view(), name='pet-detail'),
    path('vote/vote/<int:id>/', views.vote_for_pet, name='vote_for_pet'),
    path('search/', views.search_view, name='search'),
    path('profile/', views.my_profile, name='profile_detail'),
    path('leaderboardSpecies/', views.leaderboardSpecies, name='leaderboardSpecies'),


    ]



#if settings.DEBUG:
#urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
