from django.urls import path
from rest_framework.routers import DefaultRouter

from users.views import CustomUserViewset, TweetViewset, user_profile_timeline, user_home_timeline

router = DefaultRouter()

router.register(r'tweet', TweetViewset)
router.register(r'', CustomUserViewset)


urlpatterns = router.urls

urlpatterns += [
    path('<int:id>/tweets', user_profile_timeline),
    path('<int:id>/home', user_home_timeline)
]
