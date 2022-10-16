from django.contrib import admin
from django.urls import include, path

from rest_framework.authtoken import views
from rest_framework import routers

from api.views import UserViewSet, PostViewSet, GroupViewSet, CommentViewSet, FollowViewSet


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'posts', PostViewSet)
router.register(r'groups', GroupViewSet)
router.register(
    r'posts/(?P<post_id>\d+)/comments', CommentViewSet, basename='comments'
)
router.register(r'follow', FollowViewSet, basename='follow')

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/admin/', admin.site.urls),
    path('v1/api-token-auth/', views.obtain_auth_token),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
]
