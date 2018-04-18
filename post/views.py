from django.shortcuts import render,redirect

from post.models import Post

# Create your views here.
def create_post(requst):
	if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        
        post = Post.objects.create(title=title , content=content)
        return redirect('/read/?post_id=%s' % post.id)

    return render(request, 'create_post.html', {})
 

def post_list(requst):
	pass

def edit_post(requst):
	pass

def read_post(requst):
	post_id = int(request.GET.get('post_id'))
    post = Post.objects.get(id=post_id)
    return render(request, 'read_post.html',{'post':post})






