from django.db import models
from django.conf import settings
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser , PermissionsMixin
from django.db.models.signals import post_save
from PIL import Image
from rest_framework.permissions import IsAuthenticated
from django.template.defaultfilters import slugify
from django.utils import timezone
from django.db.models import Sum
import uuid
class UserAccountManager(BaseUserManager):
    def create_user(self, email, password=None, **kwargs):
       
        if not email:
            raise ValueError("Users must have an email address")
        
        email = self.normalize_email(email)
        email = email.lower()
        
        user = self.model(
            email=email,
            **kwargs
        )

        user.set_password(password)
        user.save(using=self._db)
        
        return user

    def create_superuser(self, email, password=None , **kwargs):
       
        user = self.create_user(
            email,
            password=password,
            **kwargs 
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        
        return user
    
    


class UserAccount(AbstractBaseUser , PermissionsMixin):
    first_name= models.CharField(max_length=255)
    last_name= models.CharField(max_length=255, null=True)
    artistname= models.CharField(max_length=255 , unique=True , blank=True , null=True)
    email = models.EmailField(unique=True , max_length=255)
    bio = models.TextField(blank=True)
    profile_pic = models.ImageField(
        upload_to='images/',
        null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    background = models.ImageField(
        upload_to='images/',
        null=True)
    objects = UserAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'artistname' ]
    
    def get_image(self):
        if self.profile_pic:
            return 'https://vanguardmusicss.liara.run/' + self.profile_pic.url
        return ''
    
    def get_background(self):
         if self.background:
            return 'https://vanguardmusicss.liara.run/' + self.background.url
         return ''
    
   
    def __str__(self):
        return self.email


    def views_count(self):
        
        return View1.objects.filter(views_count=self.pk)
    
    
    
    def follow_count(self):
        return Follow.objects.filter(follow_count=self.pk)

class Profile(models.Model):
    account = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='acc', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/' )
    title = models.CharField(max_length=200, null=True, blank=True)
    description = models.CharField(max_length=200, null=True, blank=True)
    track = models.FileField(upload_to='music/')
    unique_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    slug = models.SlugField(blank=True , null=True)
    key = models.SlugField(null=True , blank=True)
    ky = models.SlugField(null=True, blank=True)
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.title}'
    
    def get_image(self):
        if self.image:
            return 'https://vanguardmusicss.liara.run/' + self.image.url
        return ''
    
    def get_absolute_url(self):
        return f'/{self.slug}/'
    
   
    
    def tracks(self):
        if self.track:
            return 'https://vanguardmusicss.liara.run/' + self.track.url
        return ''
        
    def comments(self):
        ''' Get all comments '''
        return Comment.objects.filter(post__id=self.pk)
 
    def postview(self):
        
        return View1.objects.filter(postview__id=self.pk)
    
    def like(self):
        
        return Like.objects.filter(postlike__id=self.pk)
    
  
 
class Comment(models.Model):
    content = models.CharField(max_length=200, blank=True)
    post = models.ForeignKey(Profile ,on_delete=models.CASCADE, related_name='post', null=True , blank=True)
    author = models.ForeignKey(UserAccount, on_delete=models.CASCADE, related_name='author')
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True) 
    slug = models.SlugField()
    
    def get_image(self):
        return self.author.get_image()
  
    
    def __str__(self):
        return f"Comment on {self.post}"


   
    def __str__(self):
        return f"{self.content} on {self.post} by {self.author.artistname}"
     
    def get_absolute_url(self):
        return f'/{self.post.slug}/{self.slug}/'
  
    
    def get_absolute_url(self):
        return f'/{self.slug}/'
    
class Follow(models.Model):
    authorfollow = models.ForeignKey(UserAccount, on_delete=models.CASCADE, related_name='authorfollow')
    authorfollow1 = models.ForeignKey(UserAccount, on_delete=models.CASCADE, related_name='authorfollow1')
    follow_count = models.IntegerField(default=0)    
    
    
    


class View1(models.Model):
        postview = models.ForeignKey(Profile ,on_delete=models.CASCADE, related_name='postview', null=True , blank=True)
        authorview = models.ForeignKey(UserAccount, on_delete=models.CASCADE, related_name='authorview')
        views_count = models.IntegerField(default=0)
        
        @property
        def total_views(self):
            total_views_count = View1.objects.filter(postview=self.postview).aggregate(total_views=Sum('views_count'))
            total_sum = total_views_count['total_views'] if total_views_count['total_views'] else 0
            return total_sum

  

class Like(models.Model):
        postlike = models.ForeignKey(Profile ,on_delete=models.CASCADE, related_name='postlike', null=True , blank=True)
        authorlike = models.ForeignKey(UserAccount, on_delete=models.CASCADE, related_name='authorlike')
        like_count = models.IntegerField(default=0)
        
        @property
        def total_like(self):
            total_like_count = Like.objects.filter(postlike=self.postlike).aggregate(total_like=Sum('like_count'))
            total_sum = total_like_count['total_like'] if total_like_count['total_like'] else 0
            return total_sum
        
        def __str__(self):
         return f" {self.postlike} by {self.authorlike.artistname}" 