from django.contrib import admin

from posts.models import Post, Comment, Like

admin.site.register([Post, Comment, Like])
