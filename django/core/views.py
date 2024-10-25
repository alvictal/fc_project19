# Create your views here.
from django.shortcuts import render
from core.models import Post, Tag

def blog_list(request):
    # Prefetch tags to optimize queries
    posts = Post.objects.all().prefetch_related('tags')  
    tags = Tag.objects.all()
    return render(request, 'blog_list.html', {'posts': posts, 'tags':tags})