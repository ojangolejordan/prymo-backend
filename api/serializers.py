from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from api.models import Visual, Video


class UserSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password',
        )
        validators = [
            UniqueTogetherValidator(
                queryset=User.objects.all(),
                fields=['username', 'email']
            )
        ]


class VideoSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        video = Video.objects.create(**validated_data)
        return video

    class Meta:
        model = Video
        fields = (
           'title',
           'image_url',
           'video_url'
        )

class VisualSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        visual = Visual.objects.create(**validated_data)
        return visual

    class Meta:
        model = Visual
        fields = (
          "image_url",
        )
        