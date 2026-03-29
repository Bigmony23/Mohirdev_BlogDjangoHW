from django.contrib import admin

from blog.models import Post, Blog_Comment
def approve_posts(modeladmin,request, queryset):
    queryset.update(is_active=True)
approve_posts.short_description = 'Approve selected posts'

class PostAdmin(admin.ModelAdmin):
    list_display=('title','content','image','category','tegs','is_active')
    search_fields=['title']
    list_editable=['is_active']
    actions=[approve_posts]



class Blog_CommentAdmin(admin.ModelAdmin):
    list_display=('text','user')
    search_fields=['user']



admin.site.register(Post,PostAdmin)
admin.site.register(Blog_Comment,Blog_CommentAdmin)

# Register your models here.
