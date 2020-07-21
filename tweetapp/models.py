from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Tweet(models.Model):
	tweet = models.CharField(max_length=225)
	tweeter = models.OneToOneField(User, models.CASCADE)
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.tweet

	class Meta:
		db_table = "tweets"

class Like(models.Model):
	liker = models.OneToOneField(User, models.CASCADE)
	tweet = models.OneToOneField(Tweet, models.CASCADE)
	created_at = models.DateTimeField(auto_now_add=True)

	class Meta:
		db_table = "like"

class Comment(models.Model):
	comment = models.CharField(max_length=225)
	commenter = models.OneToOneField(User, models.CASCADE)
	created_at = models.DateTimeField(auto_now_add=True)

	class Meta:
		db_table = "comment"

class Follower(models.Model):
	user = models.OneToOneField(User, models.CASCADE, related_name='follower_user')
	follower = models.OneToOneField(User, models.CASCADE, related_name='follower_follower')
	created_at = models.DateTimeField(auto_now_add=True)

	class Meta:
		db_table = "follower"