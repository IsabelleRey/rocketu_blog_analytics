from blog.models import Post, Tag, Add


def latest_post(request):
    return {
        'latest_post': Post.objects.latest('created')
    }

def tags_posts(request):
    return {
        'tags_posts': Tag.objects.all()
    }

def add(request):
    return {
        'add': Add.objects.get(id=1)
    }
