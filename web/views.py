from django.shortcuts import render,redirect , get_object_or_404
from django.http import HttpResponse
from .models import Post
from web.forms import PostForm
from django.contrib import messages


def home(request):
    context = {
        'posts': Post.objects.all().order_by("-date_posted")
    }
    return render(request, 'home.html', context)

def about(request):
    return render(request, 'about.html',{'title': 'About'})

# class PostListView(ListView):

    model = Post
    context_object_name = 'posts'

def detail(request , pk):
    context = {
        'post': Post.objects.get(pk = pk) # or get_object_or_404
    }

    return render(request , 'detail.html',context)

def create(request):
    
    if request.method == "GET":
        form = PostForm()
    else:
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request, 'The post has been created successfully')
            return redirect('web-home')
    
    return render(
        request,
        'create.html',
        {'form': form}
    )