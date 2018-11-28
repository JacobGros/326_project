from django.urls import path
from PUPG import views


urlpatterns = [
    path("", views.index, name="index"),
    path("submit/", views.submit, name="submit"),
    path("leaderboard/", views.leaderboard, name="leaderboard"),
    path("vote/", views.vote, name="vote"),
    path('person/<int:pk>', views.PersonDetailView.as_view(), name='person-detail'),
    path('pet/<int:pk>', views.PetDetailView.as_view(), name='pet-detail'),
    path('vote/vote/<int:id>/', views.vote_for_pet, name='vote_for_pet'),

    
    ]



#if settings.DEBUG:
#urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
