from rest_framework import viewsets
from django.contrib.auth.models import User
from .models import Tweet, Follower, Comment, Like 
from .serializers import UserSerializer, TweetSerializer, FollowerSerializer, LikeSerializer, CommentSerializer

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class TweetViewSet(viewsets.ModelViewSet):
	queryset = Tweet.objects.all()
	serializer_class = TweetSerializer


class FollowerViewSet(viewsets.ModelViewSet):
	queryset = Follower.objects.all()
	serializer_class = FollowerSerializer


class CommentViewSet(viewsets.ModelViewSet):
	queryset = Comment.objects.all()
	serializer_class = CommentSerializer


class LikeViewSet(viewsets.ModelViewSet):
	queryset = Like.objects.all()
	serializer_class = LikeSerializer