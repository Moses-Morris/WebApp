from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.views.generic import ListView


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
    ordering = ['date']




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