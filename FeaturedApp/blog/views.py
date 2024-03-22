from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from django.contrib.auth.models import User


# Create your views here.
def index(request):
    context = {
        'posted' : Post.objects.all()
    }
    #return HttpResponse("<p>Hello, world. You're at the blog index.</p>")
    return render(request, 'index.html', context)

#class based views
class PostListView(ListView):
    model = Post
    template_name = 'index.html' #<app>/<model>_list.html
    context_object_name = 'posted'
    ordering = ['-date']
    paginate_by = 9 


class UserPostListView(ListView):
    model = Post
    template_name = 'user_posts.html' #<app>/<model>_list.html
    context_object_name = 'posted'
    #ordering = ['-date']
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date')


class PostDetailView(DetailView):
    model = Post
    template_name = 'post.html'
    

class CreatePostView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'create_post.html'
    fields = ['title', 'content']

   

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    


class UpdatePostView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = 'update_post.html'
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self): #this function is overriden by the UserPassesTestMixin
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

    


class DeletePostView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'delete_post.html'
    fields = ['title', 'content']

    success_url =  '/'

    def test_func(self): #this function is overriden by the UserPassesTestMixin
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

    








def about(request):
    #return HttpResponse("<p>Hello, world. You're at the blog about.</p>")
    return render(request, 'about.html', { 'pagename': 'About'})






posts = [
    {
        'author': 'CoreyMS',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'August 27, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'August 28, 2018'
    }

]