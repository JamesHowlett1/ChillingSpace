from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import Post

# Create your views here.
def home_view(request):
    latest_post_list = Post.objects.order_by('-pub_date')
    context = {'latest_post_list': latest_post_list}
    return render(request, 'feed/home.html', context)

def post_view(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    context = {
        'post': post,
    }

    return render(request, 'feed/post.html', context)
