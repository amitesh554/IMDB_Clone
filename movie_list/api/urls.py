from django.urls import path,include
from .views import WatchListAV,Watch_ListDetail,StreamPlatformAV,StreamPlaformDetails,ReviewList,ReviewDetails,ReviewCreate
# from rest_framework.routers import DefaultRouter


#These are frequently used when there is redundancy in urls like we want to access whole list and individual elements, then in that case Routers are best.
# router=DefaultRouter()

# router.register('stream',StreamPlatformVS,basename='streamplatform')

urlpatterns = [
     path('stream/',StreamPlatformAV.as_view()),
    path('stream/<int:pk>/',StreamPlaformDetails.as_view()),
    
    path('list/',WatchListAV.as_view()),
    path('<int:pk>/',Watch_ListDetail.as_view()),
   
    
    
    # path('review/',ReviewList.as_view()),
    # path('review/<int:pk>',ReviewDetails.as_view()),
    
    path('<int:pk>/review-create/',ReviewCreate().as_view()),
    path('<int:pk>/review/',ReviewList.as_view()),
    path('review/<int:pk>/',ReviewDetails.as_view()),
   
    
    # path('movie_list/',views.movie),
    # path('movie_list/<int:pk>',views.movie_details)
]