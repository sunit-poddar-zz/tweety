from rest_framework.routers import DefaultRouter
from django.conf.urls import include, url
from django.urls import path

from users.views import CustomUserViewset

router = DefaultRouter()

router.register(r'', CustomUserViewset)

urlpatterns = router.urls

urlpatterns += [

]