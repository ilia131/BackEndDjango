from rest_framework import serializers

from .models import Profile , UserAccount , Comment , View1 , Like , Follow
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated


from django.db.models import Sum

 






class UserAccountSerializer(serializers.ModelSerializer):
    class Meta:
        # permission_classes = [IsAuthenticated]
        model = UserAccount
        fields = ['id', 'first_name', 'last_name',  'email', 'get_image', 'get_background', 'profile_pic' , 'background' , 'artistname' ]
        
        
    def user_posts(self, account):

        posts = Profile.objects.filter(account=account)
        return ProfileSerializer(posts, many=True).data



        
        
    def user_posts1(self, account ):

        posts = Profile.objects.filter(account=account)
        return ProfileSerializer1(posts, many=True).data
    

    def user_posts2(self , unique_id):

         posts = Profile.objects.filter(unique_id=unique_id)
         return ProfileSerializer1(posts, many=True).data
    
    
    def user_posts3(self , id , *args , **kwargs):

         posts = Profile.objects.filter(id=id)
         return ProfileSerializer1(posts, many=True).data


    
    
    
    
class CommentSerializer(serializers.ModelSerializer):
    
    content = serializers.CharField(default = '', max_length=250)
    author = serializers.CharField(source='author.artistname', read_only=True)
    post = serializers.CharField(source='post.unique_id'  )
    class Meta: 
        model = Comment
        fields = ('content' ,  'id', 'author' , 'updated', 'created', 'post' , 'get_image' )
        
class CommentSerializer2(serializers.ModelSerializer):
     
    content = serializers.CharField(default = '', max_length=250)
    author = serializers.CharField(source='author.artistname', read_only=True)
    post = serializers.CharField( )
    class Meta: 
        model = Comment
        fields = ('content' ,  'id', 'author' , 'updated', 'created' , 'post'  , 'get_image')        




class CommentSerializer1(serializers.ModelSerializer):
   
    content = serializers.CharField(default = '', max_length=250)
    author = serializers.CharField(source='author.artistname', read_only=True)
    post = serializers.CharField()
    class Meta: 
        model = Comment
        fields = ('content' ,  'id', 'author' , 'updated', 'created', 'post'  , 'get_image' )


class ShowSerlizer1(serializers.ModelSerializer):
    authorview = serializers.CharField(source='authorview.artistname', read_only=True)
    postview = serializers.CharField(source='postview.unique_id')
    views_count = serializers.IntegerField(default=0)
    class Meta:
        model = View1
        fields = ('id' , 'views_count'  , 'postview' , 'authorview')
    
        
        
class ShowSerlizer9(serializers.ModelSerializer):
     total_views = serializers.IntegerField(read_only=True)
     authorview = serializers.CharField(source='authorview.artistname', read_only=True)
     postview = serializers.CharField(source='postview.unique_id')
     views_count = serializers.IntegerField(default=0)
     class Meta:
        model = View1
        fields = ('id' , 'views_count'  , 'postview' , 'authorview' , 'total_views')  
        
    
   

class LikeSerilizer(serializers.ModelSerializer):
    authorlike = serializers.CharField(source='authorlike.artistname', read_only=True)
    postlike = serializers.CharField(source='postlike.unique_id')
    like_count = serializers.IntegerField(default=0)
    class Meta:
        model = Like
        fields = ('id' , 'like_count', 'postlike' , 'authorlike')  

class LikeSerilizer10(serializers.ModelSerializer):
    total_like = serializers.IntegerField(read_only=True)
    authorlike = serializers.CharField(source='authorlike.artistname', read_only=True)
    postlike = serializers.CharField(source='postlike.unique_id')
    like_count = serializers.IntegerField(default=0)
    class Meta:
        model = Like
        fields = ('id' , 'like_count', 'postlike' , 'authorlike' , 'total_like') 

        
        
class FollowSerilizer(serializers.ModelSerializer):
    followerpic = serializers.ImageField(source ='authorfollow.profile_pic' , read_only=True)
    authorfollow = serializers.CharField(source='authorfollow.artistname', read_only=True)
    authorfollow1 = serializers.CharField(source='authorfollow1.artistname')
    followingpic1 = serializers.ImageField(source = 'authorfollow1.profile_pic', read_only=True)
    follow_count = serializers.IntegerField(default=0)
    
    class Meta:
        model = Follow
        fields = ('id' , 'follow_count', 'authorfollow', 'authorfollow1' , 'followerpic' , 'followingpic1')
    
    
class ProfileSerializer(serializers.ModelSerializer):
    # comments = CommentSerializer(many=True , required=False) 
    image = serializers.ImageField(default='avatar.png'  ,allow_empty_file=False)
    track = serializers.FileField(default='avatar.png' ,max_length=None,allow_empty_file=False )
    title = serializers.CharField(default='avatar.png',max_length=250 ,)
    description = serializers.CharField(default='avatar.png',max_length=250)
    class Meta:  
        model = Profile
        fields = ('id', 'title', 'description' , 'unique_id'  , 'image', 'get_image', 'track', 'tracks', 'unique_id',  ) #if have problem add 'account'  
    
    def user_comment(self, unique_id):

        comment = Comment.objects.filter(unique_id=unique_id)
        return Comment(comment, many=True).data
    
    def user_comment1(self, artistname):

        comment = Comment.objects.filter(artistname=artistname)
        return Comment(comment, many=True).data

class ProfileSerializer103(serializers.ModelSerializer):
    # comments = CommentSerializer(many=True , required=False) 
    image = serializers.ImageField(default='avatar.png'  ,allow_empty_file=False)
    track = serializers.FileField(default='avatar.png' ,max_length=None,allow_empty_file=False )
    title = serializers.CharField(default='avatar.png',max_length=250 ,)
    description = serializers.CharField(default='avatar.png',max_length=250)
    total_views = serializers.SerializerMethodField()

    class Meta:  
        model = Profile
        fields = ('id', 'title', 'description' , 'unique_id'  , 'image', 'get_image', 'track', 'tracks', 'unique_id', 'total_views' )

    
    def get_total_views(self, obj):
        total_views_count = View1.objects.filter(postview=obj).aggregate(total_views=Sum('views_count'))
        total_sum = total_views_count['total_views'] if total_views_count['total_views'] else 0
        return total_sum






    
    
    
class ProfileSerializer8(serializers.ModelSerializer):
    account = serializers.CharField(source='account.artistname')
    postview=ShowSerlizer9(many=True)
    like = LikeSerilizer(many=True)
    comments = CommentSerializer(many=True) 
    image = serializers.ImageField(default='avatar.png'  ,allow_empty_file=False)
    track = serializers.FileField(default='avatar.png' ,max_length=None,allow_empty_file=False )
    title = serializers.CharField(default='avatar.png',max_length=250 ,)
    description = serializers.CharField(default='avatar.png',max_length=250)
    total_views = serializers.SerializerMethodField()
    class Meta:  
        model = Profile
        fields = ( 'total_views', 'id', 'title', 'description' , 'unique_id'  , 'image', 'get_image', 'track', 'tracks' , 'comments' , 'postview', 'like' ,'account' )    
    
    def get_total_views(self, obj):
        total_views_count = View1.objects.filter(postview=obj).aggregate(total_views=Sum('views_count'))
        total_sum = total_views_count['total_views'] if total_views_count['total_views'] else 0
        return total_sum


class ProfileSerializer100(serializers.ModelSerializer):
    account = serializers.CharField(source='account.artistname')
    total_like=serializers.SerializerMethodField()
    postlike = LikeSerilizer10(many=True)
    postview=ShowSerlizer1(many=True)
    image = serializers.ImageField(default='avatar.png'  ,allow_empty_file=False)
    track = serializers.FileField(default='avatar.png' ,max_length=None,allow_empty_file=False )
    title = serializers.CharField(default='avatar.png',max_length=250 ,)
    description = serializers.CharField(default='avatar.png',max_length=250)
    
    class Meta:  
        model = Profile
        fields = ( 'id', 'title', 'description' , 'unique_id'  , 'image', 'get_image', 'track', 'tracks'  , 'postview', 'postlike' ,'account'  , 'total_like')    
    
    def get_total_like(self, obj):
        total_like_count = Like.objects.filter(postlike=obj).aggregate(total_like=Sum('like_count'))
        total_sum = total_like_count['total_like'] if total_like_count['total_like'] else 0
        return total_sum


class ProfileSerializer101(serializers.ModelSerializer):
      total = serializers.IntegerField()

      class Meta:
        model = View1
        fields = ['total']



class ProfileSerializer12(serializers.ModelSerializer):
    class Meta :
        model = Profile
        fields = '__all__'





  



class LikeSerilizer20(serializers.ModelSerializer):
    profileliked = serializers.SerializerMethodField()
    authorlike = serializers.CharField(source='authorlike.artistname', read_only=True)
    postlike = serializers.CharField(source='postlike.unique_id')
    like_count = serializers.IntegerField(default=0)
    class Meta:
        model = Like
        fields = ('id' , 'like_count', 'postlike' , 'authorlike' , 'profileliked' )  

    
    def get_profileliked(self ,instance):
     
        profile = Profile.objects.all()
        return ProfileSerializer12(profile).data
   









    
    # def to_representation(self, instance):
    #     ret = super(ProfileSerializer8, self).to_representation(instance)
    #     ret['postview'] = sorted(ret['postview'], key=lambda x: x['total_views'], reverse=True)
    #     return ret
    
    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     queryset = queryset.annotate(total_views=Sum('postview__views_count')).order_by('total_views')
    #     return queryset
    







    
    
class ProfileSerializer1(serializers.ModelSerializer):
    postview=ShowSerlizer1(many=True)
    like = LikeSerilizer(many=True)
    comments = CommentSerializer(many=True) 
    image = serializers.ImageField(default='avatar.png'  ,allow_empty_file=False)
    track = serializers.FileField(default='avatar.png' ,max_length=None,allow_empty_file=False )
    title = serializers.CharField(default='avatar.png',max_length=250 ,)
    description = serializers.CharField(default='avatar.png',max_length=250)
    class Meta:  
        model = Profile
        fields = ('id', 'title', 'description' , 'unique_id'  , 'image', 'get_image', 'track', 'tracks' , 'comments' , 'postview', 'like' )    




class ProfileSerializer2(serializers.ModelSerializer):
   
    comments = CommentSerializer(many=True) 
    image = serializers.ImageField(default='avatar.png'  ,allow_empty_file=False)
    track = serializers.FileField(default='avatar.png' ,max_length=None,allow_empty_file=False )
    title = serializers.CharField(default='avatar.png',max_length=250 ,)
    description = serializers.CharField(default='avatar.png',max_length=250)
    class Meta:  
        model = Profile
        fields = ('id', 'title', 'description' , 'slug', 'unique_id'  , 'image', 'get_image', 'track', 'tracks' , 'comments' , 'key', 'ky')   







    
    
class ProfileSerializer3(serializers.ModelSerializer):
   
  
    class Meta:  
        model = Profile
        fields = '__all__'  
    
        
  
    

