from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy
from articles.forms import PostForm
from articles.models import Post
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin



class PostView(LoginRequiredMixin,CreateView):
    template_name = 'article/post.html'
    model = Post
    form_class = PostForm



    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(PostView, self).form_valid(form)
    
    def form_invalid(self, form):
        return redirect('articles:post')
    
    success_url = reverse_lazy('articles:home')

class PostListView(LoginRequiredMixin,ListView):
    model = Post
    template_name = 'account/home.html'

    
