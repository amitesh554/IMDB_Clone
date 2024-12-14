from rest_framework import serializers
from movie_list.models import WatchList,StreamPlatform,Reviews

class ReviewSerializer(serializers.ModelSerializer):
    user_name=serializers.StringRelatedField(read_only=True)
    class Meta:
        model=Reviews
       
        exclude=('watchlist',)

class WatchListSerializers(serializers.ModelSerializer):
  
    reviews=ReviewSerializer(many=True,read_only=True) 
    platform=serializers.CharField(source='platform.name')
    class Meta:
        model=WatchList
        fields="__all__"
        
        
class StreamPlatformSerializers(serializers.ModelSerializer):
   
    
    watchlist=WatchListSerializers(many=True,read_only=True) 
    
    class Meta:
        model=StreamPlatform
        fields="__all__"
        
        
        
        
        
        
        
  