from urllib import request

from django.shortcuts import render, redirect

from post.models import Post


# Create your views here.
def create_post(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        post = Post.objects.create(title=title, content=content)
        return redirect('/post/read/?post_id=%s' % post.id)

    return render(request, 'create.html', {})


def post_list(request):
    pass


def edit_post(request):
    pass


def read_post(request):
    post_id = int(request.GET.get('post_id'))
    post = Post.objects.get(id='post_id')
    return render(request, 'read_post.html', {'post': post})
