from rest_framework import routers
from django.urls import include, path
from tweetapp.views import UserViewSet, TweetViewSet, FollowerViewSet, CommentViewSet, LikeViewSet

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'tweets', TweetViewSet)
router.register(r'like', LikeViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'followers', FollowerViewSet)

urlpatterns = [
    path(r'', include(router.urls)),
]