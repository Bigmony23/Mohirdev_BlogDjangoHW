from django.contrib import admin

from blog.models import Post, Blog_Comment


class PostAdmin(admin.ModelAdmin):
    list_display=('title','content','image','category','tegs')
    search_fields=['title']

class Blog_CommentAdmin(admin.ModelAdmin):
    list_display=('text','user')
    search_fields=['user']

admin.site.register(Post,PostAdmin)
admin.site.register(Blog_Comment,Blog_CommentAdmin)

# Register your models here.
