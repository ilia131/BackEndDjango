from django.urls import path , include , re_path
from rest_framework import routers
from .views import (
    CustomTokenObtainPairView,
    CustomTokenRefreshView,
    CustomTokenVerifyView,
    LogoutView,
    ProfileList,
    RetrieveUser,
    RetrieveUser1,
    # EmailVerificationAPIView
    # CurrentUserView,
    
)
from userartist import views
from . import views
router = routers.SimpleRouter()
# router.register(r'users', views.UserViewSet)

router = routers.DefaultRouter()
router.register('profile', views.ProfileViewSet, basename='profile')
router.register('user2', views.RetrieveUser, basename='userid')
router.register('userMe6', views.UuuidView , basename='uuid')
router.register('vie4', views.ShowAllView , basename='vie4')
router.register('viesum', views.ShowSumView , basename='vie4')
router.register('allvi4', views.ShowAllView1 , basename='allvie4')

router.register('like', views.ShowLike , basename='like')
router.register('follow', views.ShowFollow , basename='follow')
router.register('follower', views.ShowFollower , basename='follow')
router.register('likeuser' , views.LikeDeleteView , basename='likeuser'),
router.register('followuser' , views.FollowDeleteView , basename='followuser'),




urlpatterns = [
    re_path(r'^o/(?P<provider>\S+)/$', views.CustomProviderAuthView.as_view(), name='provider-auth'),
    path('jwt/create/', CustomTokenObtainPairView.as_view()),
    path('jwt/refresh/', CustomTokenRefreshView.as_view()),
    path('jwt/verify/', CustomTokenVerifyView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('profile/<int:pk>', ProfileList.as_view(),),
    path('userid/<int:pk>', RetrieveUser1.as_view()),
    path('userME/', views.UserViewSetChild.as_view() , name='users-me'),
    path('generics/<pk>/' , views.PostApiView.as_view()),
    path('total/' , views.TotalViewsCountAPIView.as_view()),
    path('userME1/', views.UserViewSetChild1.as_view() , name='users-me'),
    path('userME2/', views.UserViewSetChild2.as_view() , name='users-me'),
    path('userME3/', views.UserViewSetChild3.as_view() , name='users-me'),
    path('userME4/<int:pk>/', views.ProfileDetailsView().as_view, name='user-me1'),
    path('add-comment-to-post/',views.AddCommentToPost.as_view(), name='add-comment-to-post'),
    path('p/<slug:profile_slug>/<slug:comment_slug>/', views.UploadmusicVUE.as_view()),
    path('', include(router.urls))
]
