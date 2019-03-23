from rest_framework import serializers
from . import models

class HelloSerializer(serializers.Serializer):
    """Serializers a name field for testing our APIView."""

    name=serializers.CharField(max_length=10)

class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model=models.Userprofile
        fields=('id','email','name','password')
        extra_kwargs={'password':{'write_only':True}}

    def create(self,validated_data):
        """create a return a new user."""

        user=models.Userprofile(
            email=validated_data['email'],
            name=validated_data['name']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

class ProfileFeedSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.ProfileFeedItem
        fields=('id','user_profile','status_text','created_on')
        extra_kwargs = {'user_profile': {'read_only': True}}