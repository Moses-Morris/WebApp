from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin



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


class UpdatePostView(LoginRequiredMixin, UpdateView):
    model = Post
    template_name = 'update_post.html'
    fields = ['title', 'content']







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