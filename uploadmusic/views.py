from django.shortcuts import render
from rest_framework.decorators import action
# Create your views here.
from django.shortcuts import render
from rest_framework.decorators import api_view
from django.db.models import Q
from rest_framework import generics , mixins , viewsets
# Create your views here.
# from rest_framework.filters import SearchFilter
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UploadmusicSerializer , VideoSerializer
from .models import Uploadmusic , Video
from django.http import Http404 , HttpResponse
from django.core.mail import send_mail
from rest_framework.permissions import AllowAny
from userartist.models import Profile , UserAccount , Comment , Like , View1
from userartist.serializers import (ProfileSerializer ,
UserAccountSerializer , CommentSerializer , ProfileSerializer2 , 
CommentSerializer2 , ProfileSerializer1 , ProfileSerializer8 ,
ProfileSerializer100 , LikeSerilizer10 , LikeSerilizer,
LikeSerilizer20, ProfileSerializer12 , ProfileSerializer101 , ProfileSerializer103
)
from django.shortcuts import get_object_or_404
from django.db.models import Sum

# def send_email(request):
#     subject = 'Django'
#     message = 'From Django Hello'
#     from_email = 'info@vanguardmusics.ir'
#     recipient_list = ['iliagholami151@gmail.com']
    
#     send_mail(subject, message,from_email, recipient_list, fail_silently=False)
    
#     return HttpResponse('Success')


# class UploadmusicView(APIView):
#     permission_classes = [AllowAny]
#     def get(self, request):
#         queryset = Uploadmusic.objects.all()
#         serializer = UploadmusicSerializer(queryset, many=True)
        
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = UploadmusicSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=201)
#         return Response(serializer.errors, status=400)



class PostView(APIView):
       permission_classes = [AllowAny]
       def get(self, request):
         queryset = Profile.objects.annotate(total_views=Sum('postview__views_count')).order_by('-total_views')
         serializer = ProfileSerializer8(queryset, many=True)
         return Response(serializer.data)











class PostLike(APIView):
    permission_classes = [AllowAny]
    def get(self, request):
        queryset = Profile.objects.annotate(total_like=Sum('postlike__like_count')).order_by('-total_like')
        serializer = ProfileSerializer100(queryset, many=True)
        return Response(serializer.data)
    
class AllMusicView(APIView):
    permission_classess = [AllowAny]
    def get(self , request):
        queryset = Profile.objects.all()
        serializer = ProfileSerializer1(queryset , many=True)
        return Response(serializer.data)


class VideoView(APIView):
    permission_classes = [AllowAny]
    def get(self, request):
        queryset = Video.objects.all()
        serializer = VideoSerializer(queryset, many=True)
        
        return Response(serializer.data)



class UploadmusicView(APIView):
    permission_classes = [AllowAny]
    def get(self, request):
        queryset = Uploadmusic.objects.all()
        serializer = UploadmusicSerializer(queryset, many=True)
        
        return Response(serializer.data)

    
    
class UploadmusicViewT(APIView):
    def get(self, request):
        queryset = Uploadmusic.objects.all()[0:4]
        serializer = UploadmusicSerializer(queryset, many=True)
        
        return Response(serializer.data)

    def post(self, request):
        serializer = UploadmusicSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
        
    
    
    
    
    
    
    
    
    
    
class UploadmusicDetail(APIView):
    def get_object(self, uploadmusic_slug, artists_slug):
        try:
            return Uploadmusic.objects.filter(uploadmusic__slug=uploadmusic_slug).get(slug=artists_slug)
        except Uploadmusic.DoesNotExist:
            raise Http404
    
    def get(self, request, uploadmusic_slug, artists_slug, format=None):
        queryset = self.get_object(uploadmusic_slug, artists_slug)
        serializer = UploadmusicSerializer(queryset)
        return Response(serializer.data)


    
    
    



class UploadmusicTitle(viewsets.GenericViewSet, mixins.ListModelMixin):
     queryset = Uploadmusic.objects.all()
     serializer_class = UploadmusicSerializer
     
     def get_queryset(self):
         adamid = self.request.query_params.get('query', None)
         if not adamid: 
             return self.queryset
         
         return self.queryset.filter(adamid=adamid)


class UploadmusicSearchViewSett(viewsets.GenericViewSet, mixins.ListModelMixin):
     queryset = Uploadmusic.objects.all()
     serializer_class = UploadmusicSerializer
     
     def get_queryset(self):
         text = self.request.query_params.get('query', None)
         if not text: 
             return self.queryset
         
         return self.queryset.filter(title__icontains=text)







class UploadmusicSearchViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
     permission_classes = [AllowAny]

     queryset = Profile.objects.all()
     serializer_class = ProfileSerializer8
     
     def get_queryset(self):
         text = self.request.query_params.get('query', None)
         if not text: 
             return self.queryset
         
         return self.queryset.filter(Q(title__icontains=text) | Q(description__icontains=text) | Q(account__artistname__icontains=text))
     
     

class UploadmusicsSongKey(viewsets.GenericViewSet, mixins.ListModelMixin):
     
     permission_classes = [AllowAny]

     queryset = Profile.objects.all()
     serializer_class = ProfileSerializer2
     
     def get_queryset(self):
         ky = self.request.query_params.get('query', None)
         if not ky:
              return self.queryset
          
         return self.queryset.filter(ky__icontains=ky)
     


class UploadmusicSongKey(viewsets.GenericViewSet, mixins.ListModelMixin):
     permission_classes = [AllowAny]

     queryset = Profile.objects.all()
     serializer_class = ProfileSerializer2
     
     def get_queryset(self):
         key = self.request.query_params.get('query', None)
         if not key:
              return self.queryset
          
         return self.queryset.filter(key=key)









# class UploadmusicSongKey(viewsets.GenericViewSet, mixins.ListModelMixin):
#      permission_classes = [AllowAny]

#      queryset = Uploadmusic.objects.all()
#      serializer_class = UploadmusicSerializer
     
#      def get_queryset(self):
#          key = self.request.query_params.get('query', None)
#          if not key:
#               return self.queryset
          
#          return self.queryset.filter(key=key)
 
class ShowPostUser(viewsets.GenericViewSet, mixins.ListModelMixin):
    permission_classes = [AllowAny]
    serializer_class = ProfileSerializer 
    def get_serializer_class(self):
        if self.action == 'list':
            return ProfileSerializer
        elif self.action == 'create_comment':
            return CommentSerializer2
        else:
            return super().get_serializer_class()
   
    
    
    
    
    def get_queryset(self):
        text = self.request.query_params.get('query', None)

        if not text:
            return Profile.objects.all()
        
        profiles = Profile.objects.filter(Q(account__artistname=text))
        user_accounts = UserAccount.objects.filter(Q(artistname=text))
        comment = Comment.objects.filter(Q(author__artistname=text))
        return profiles, user_accounts , comment , 

    def list(self, request, *args, **kwargs):
        profiles, user_accounts , comment = self.get_queryset()
    
        profile_serializer = ProfileSerializer103(profiles, many=True)
        user_account_serializer = UserAccountSerializer(user_accounts, many=True)
        comment_serializer = CommentSerializer2(comment, many=True)
        return Response({
            'profiles': profile_serializer.data,
            'user_accounts': user_account_serializer.data,
            'comment': comment_serializer.data
        })
    
# class UserShowPost2(mixins.CreateModelMixin, generics.RetrieveAPIView):
#     serializer_class = CommentSerializer
#     permission_classes = [AllowAny]

    
        
#     def get(self , request , *arg , **kwargs):
#         unique_id = kwargs.get('unique_id')
#         serializer = UserAccountSerializer()
#         posts = serializer.user_posts2(unique_id)
#         data = serializer.data
#         data['posts'] = posts
#         return Response(data)   
   
 
 
 
 
 
 
 
 




 
 
 
 
 
 
 
 
 
 
     

class UploadmusicSlug(viewsets.GenericViewSet, mixins.ListModelMixin):
     permission_classes = [AllowAny]
     queryset = Uploadmusic.objects.all()
     serializer_class = UploadmusicSerializer
     
     def get_queryset(self):
         slug = self.request.query_params.get('query', None)
         if not slug:
              return self.queryset
          
         return self.queryset.filter(slug=slug)     
     
     
     
class PostSlug(viewsets.GenericViewSet, mixins.ListModelMixin):
     permission_classes = [AllowAny]
     queryset = Profile.objects.all()
     serializer_class = ProfileSerializer2
     
     def get_queryset(self):
         slug = self.request.query_params.get('query', None)
         if not slug:
              return self.queryset
          
         return self.queryset.filter(slug=slug)     
     
     
     
     



     
     
     
     
     
     
  
     
     
     
class UploadmusicArtists(viewsets.GenericViewSet, mixins.ListModelMixin):
    
    queryset = Uploadmusic.objects.all()
    serializer_class = UploadmusicSerializer
  
     
     
    def get_queryset(self):
         artists = self.request.query_params.get('query', None)
         if not artists:
              return self.queryset
          
         return self.queryset.filter(artists=artists)
     
     
     
     
class UploadmusicVUE(APIView):
    def get_object(self, category_slug, uploadmusic):
        try:
            return Uploadmusic.objects.filter(category__slug=category_slug).get(slug=uploadmusic)
        except Uploadmusic.DoesNotExist:
            raise Http404
    
    def get(self, request, category_slug, uploadmusic_slug, format=None):
        query = self.get_object(category_slug, uploadmusic_slug)
        serializer = UploadmusicSerializer(query)
        return Response(serializer.data)
    
