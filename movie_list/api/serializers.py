from rest_framework import serializers
from movie_list.models import WatchList,StreamPlatform,Reviews

class ReviewSerializer(serializers.ModelSerializer):
    user_name=serializers.StringRelatedField(read_only=True)
    class Meta:
        model=Reviews
        # fields="__all__"
        exclude=('watchlist',)

class WatchListSerializers(serializers.ModelSerializer):
    
    #We have to take care of names while writing here.It should match related_names if we want to show in output. For ex- Here it is reviews. And if we have not used related_names then we fields name should match like "user_name" mentioned above.
    
    reviews=ReviewSerializer(many=True,read_only=True) #Each Watchlist can have multiple reviews
    platform=serializers.CharField(source='platform.name')
    class Meta:
        model=WatchList
        fields="__all__"
        
        
class StreamPlatformSerializers(serializers.ModelSerializer):
    #Use same Keyword that is used in related_name in models in foreign key i.e. watchlist
    
    watchlist=WatchListSerializers(many=True,read_only=True) #Each stream can have multiple watchlist
    
    #watchlist=serializers.StringRelatedField(many=True)  #This return only def_str_() function field of that model not all fields
    
    class Meta:
        model=StreamPlatform
        fields="__all__"
        
        
        
        
        
        
        
        
        # fields=['id','name','description']
        # exclude=['name']
    # def validate_name(self,value):
    #     if len(value)<2:
    #         raise serializers.ValidationError("Name is short")
    #     else:
    #         return value

# class MovieSerializers(serializers.Serializer):
#     id=serializers.IntegerField(read_only=True)
#     name=serializers.CharField()
#     description=serializers.CharField()
#     active=serializers.BooleanField()
    
#     def create(self,validated_data):
#         return Movie.objects.create(**validated_data)
    
#     def update(self,instance,validated_data):
#         instance.name=validated_data.get('name',instance.name)
#         instance.description=validated_data.get('description',instance.description)
#         instance.active=validated_data.get('active',instance.active)
#         instance.save() 
#         return instance
    
#     def validate_name(self,value):
#         if len(value)<2:
#             raise serializers.ValidationError("Name is short")
#         else:
#             return value