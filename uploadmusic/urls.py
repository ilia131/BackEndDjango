from django.urls import path , include
from .views import ( UploadmusicView , UploadmusicDetail
 , UploadmusicViewT ,
 UploadmusicArtists 
, UploadmusicVUE , UploadmusicSlug
, UploadmusicTitle, 
PostView , PostSlug)
from django.conf import settings
from django.conf.urls.static import static
from uploadmusic import views
from rest_framework.schemas import get_schema_view

from rest_framework import routers

router = routers.DefaultRouter()
router.register('search', views.UploadmusicSearchViewSet, basename='search-music')
router.register('title', views.UploadmusicTitle, basename='title-music')
router.register('songskey', views.UploadmusicSongKey, basename='key-music')
router.register('artistname', views.ShowPostUser, basename='key-artistname')
router.register('songsket', views.UploadmusicsSongKey, basename='key-musics')
# router.register('slug', views.UploadmusicSlug, basename='slug-music')
router.register('slug', views.PostSlug, basename='slug-music')

router.register('songartist', views.UploadmusicArtists, basename='song-artist')


urlpatterns = [
    # path('', UploadmusicView.as_view()),
    path('', PostView.as_view()),
    path('alllike/', views.PostLike.as_view()),
    path('musics/', views.AllMusicView.as_view()),
    path('songt/',  UploadmusicViewT.as_view()),
    path('songs/', UploadmusicView.as_view()),
    path('video/', views.VideoView.as_view()),
    # path('send-email/', views.send_email , name='send_email'),
    path('', include(router.urls))
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

app_name='music'