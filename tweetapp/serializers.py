from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Tweet, Follower, Like, Comment

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = User
		fields = ['url', 'username', 'email', 'is_staff']

class UserMiniSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = User
		fields = ['username']


class TweetSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Tweet
		fields = '__all__'

class LikeSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Like
		fields = '__all__'

class CommentSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Comment
		fields = '__all__'

class FollowerSerializer(serializers.HyperlinkedModelSerializer):
	user = UserMiniSerializer(many=False)
	"""
	def to_representation(self, instance):
		ret = super().to_representation(instance)
		ret['follower'] = ret['user']['username']
		return ret"""
	class Meta:
		model = Follower
		fields = [ 'user', 'follower' ]