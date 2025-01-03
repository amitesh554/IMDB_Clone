from .serializers import WatchListSerializers,StreamPlatformSerializers,ReviewSerializer
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from movie_list.models import WatchList,StreamPlatform,Reviews
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework import status
# from rest_framework import mixins
from rest_framework import generics,viewsets
from .permissions import AdminOrReadOnly,ReviewUserOrReadOnly,IsAuthenticated




class ReviewCreate(generics.CreateAPIView):
    permission_classes=[IsAuthenticated]
   
    serializer_class=ReviewSerializer
    
    def get_queryset(self):
        return Reviews.objects.all()
    
    def perform_create(self, serializer):
        pk=self.kwargs.get('pk')
        watchlist=WatchList.objects.get(pk=pk)
        
        user_name=self.request.user
        user_queryset=Reviews.objects.filter(watchlist=watchlist,user_name=user_name)
        
        if user_queryset.exists():
            raise ValidationError("This user already exists")
        
      
        if watchlist.avg_rating==0:
            watchlist.avg_rating=serializer.validated_data['rating']
        else:
            watchlist.avg_rating=(watchlist.avg_rating+serializer.validated_data['rating'])/2
            
        watchlist.total_rating=watchlist.total_rating+1
        watchlist.save()
            
        serializer.save(watchlist=watchlist,user_name=user_name)

class ReviewList(generics.ListAPIView):
     
    serializer_class=ReviewSerializer
 
    def get_queryset(self):
        pk=self.kwargs['pk']
        return Reviews.objects.filter(watchlist=pk)
    
class ReviewDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset=Reviews.objects.all()
    serializer_class=ReviewSerializer
    permission_classes=[ReviewUserOrReadOnly]
   


class WatchListAV(APIView):
    permission_classes=[IsAuthenticated]
    
    def get(self,request):
        movies=WatchList.objects.all()
        serializer=WatchListSerializers(movies,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer=WatchListSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
class Watch_ListDetail(APIView):
    permission_classes=[AdminOrReadOnly]
    
    def put(self,request,pk):
        try:
            movie=WatchList.objects.get(pk=pk)
        except WatchList.DoesNotExist:
          return Response({'Error':'Movie not found'},status=status.HTTP_404_NOT_FOUND)
        serializer=WatchListSerializers(movie,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    
    def delete(self,request,pk):
        try:
            movie=WatchList.objects.get(pk=pk)
        except WatchList.DoesNotExist:
            return Response({'Error':'Movie not found'},status=status.HTTP_404_NOT_FOUND)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    

class StreamPlatformAV(APIView):
    permission_classes=[AdminOrReadOnly]
    
    def get(self,request):
        platform=StreamPlatform.objects.all()
        serializer=StreamPlatformSerializers(platform,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer=StreamPlatformSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
            

class StreamPlaformDetails(APIView):
    permission_classes=[AdminOrReadOnly]
    
    def get(self,request,pk):
        platform=StreamPlatform.objects.get(pk=pk)
        serializer=StreamPlatformSerializers(platform)
        return Response(serializer.data)
    
    def put(self,request,pk):
        try:
            platform=StreamPlatform.objects.get(pk=pk)
        except StreamPlatform.DoesNotExist:
            return Response({'Error':"Not found"},status=status.HTTP_404_NOT_FOUND)
        
        serializer=StreamPlatformSerializers(platform,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self,request,pk):
        try:
            platform=StreamPlatform.objects.get(pk=pk)
        except StreamPlatform.DoesNotExist:
            return Response({'Error':"Not found"},status=status.HTTP_404_NOT_FOUND)
        platform.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
             
