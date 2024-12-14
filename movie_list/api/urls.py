from django.urls import path,include
from .views import WatchListAV,Watch_ListDetail,StreamPlatformAV,StreamPlaformDetails,ReviewList,ReviewDetails,ReviewCreate


urlpatterns = [
     path('stream/',StreamPlatformAV.as_view()),
    path('stream/<int:pk>/',StreamPlaformDetails.as_view()),
    
    path('list/',WatchListAV.as_view()),
    path('<int:pk>/',Watch_ListDetail.as_view()),

    
    path('<int:pk>/review-create/',ReviewCreate().as_view()),
    path('<int:pk>/review/',ReviewList.as_view()),
    path('review/<int:pk>/',ReviewDetails.as_view()),

]