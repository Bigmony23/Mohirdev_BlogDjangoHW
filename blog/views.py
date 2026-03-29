from datetime import timedelta

from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import F
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils import timezone
from django.views import View

from blog.forms import AddPostForm, AddCommentForm
from blog.models import Post, Blog_Comment


class HomeView(View):
    def get(self, request):
        context = {
            'latest_posts':Post.objects.filter(is_active=True).order_by('-id')[:5],
            'popular_posts':Post.objects.filter(is_active=True).order_by('-views')[:5],
            'weekly_posts':Post.objects.filter(is_active=True,created_at__gte=timezone.now()-timedelta(days=7)).order_by('-created_at')[:5],
            'monthly_posts':Post.objects.filter(is_active=True,created_at__gte=timezone.now()-timedelta(days=30)).order_by('-created_at')[:5],
        }
        return render(request,'home.html',context)
# Create your views here.
class AddPostView(LoginRequiredMixin,View):
    def get(self, request):
        post_form = AddPostForm()
        return render(request,'add_post.html',{'post_form':post_form})
    def post(self, request):
        post_form=AddPostForm(request.POST,request.FILES)
        if post_form.is_valid():
            post = post_form.save(commit=False)
            post.user=request.user
            post.save()
            return redirect('home')
        return render(request,'add_post.html',{'post_form':post_form})
class PostListView(View):
    def get(self, request):
        posts = Post.objects.all().filter(is_active=True)
        return render(request,'posts.html',{'posts':posts})

class PostDetailView(View):
    def get(self, request, id):
        Post.objects.filter(id=id).update(views=F('views')+1)
        post = Post.objects.get(id=id)

        comment_form=AddCommentForm()
        context={'post':post,'comment_form':comment_form}
        return render(request,'post_detail.html',context)

class AddCommentView(LoginRequiredMixin,View):
    def post(self, request,id):
        post=Post.objects.get(id=id)
        comment_form=AddCommentForm(request.POST)
        if comment_form.is_valid():
            Blog_Comment.objects.create(user=request.user,
                                        post=post,
                                        text=comment_form.cleaned_data['text']
                                        )

        return redirect('post_detail',id=post.id)

