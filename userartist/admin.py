from django.contrib import admin

from .models import Profile , UserAccount , Comment , View1 , Like , Follow

admin.site.register(Profile)
admin.site.register(UserAccount)
admin.site.register(Comment)
admin.site.register(View1)
admin.site.register(Like)
admin.site.register(Follow)