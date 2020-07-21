from django.contrib import admin
from .models import Tweet, Follower, Like, Comment

# Register your models her
admin.site.register(Tweet)
admin.site.register(Like)
admin.site.register(Comment)
admin.site.register(Follower)