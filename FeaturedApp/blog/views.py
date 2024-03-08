from django.shortcuts import render
from django.http import HttpResponse


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
# Create your views here.
def index(request):
    context = {
        'posted' : posts
    }
    #return HttpResponse("<p>Hello, world. You're at the blog index.</p>")
    return render(request, 'index.html', context)



def about(request):
    #return HttpResponse("<p>Hello, world. You're at the blog about.</p>")
    return render(request, 'about.html', { 'pagename': 'About'})