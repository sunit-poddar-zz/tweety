from rest_framework.routers import DefaultRouter

from users.views import CustomUserViewset

router = DefaultRouter()

router.register(r'', CustomUserViewset)

urlpatterns = router.urls

urlpatterns += [

]