from django.shortcuts import render, get_object_or_404
from analytics.models import Page
from blog.models import Post, Add


def blog(request):

    return render(request, 'blog.html', {
        'posts': Post.objects.order_by('-created')
    })


def post(request, pk):
    post_obj = get_object_or_404(Post, pk=pk)

    return render(request, 'post.html', {
        'post': post_obj
    })

def tag(request, tag_name):
    tags = Post.objects.filter(tags__name=tag_name)
    return render(request, 'blog.html', {
        'posts': tags
    })


def add(request):
    # adds = Add.objects.filter(state=state)
    adds = Add.objects.all().order_by('?')[0]
    # add=[]
    # random_add=get.random
    return render(request, 'blog.html', {
        'add': adds
    })

def page(request, page_url):
    pages = Page.objects.filter(page_url=page_url)
    return render(request, 'main.html'),{
        'pages' : pages
    }