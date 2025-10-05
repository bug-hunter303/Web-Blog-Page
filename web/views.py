from django.shortcuts import render,redirect , get_object_or_404
from django.http import HttpResponse
from .models import Post
from web.forms import PostForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.contrib.auth.models import User


def home(request):
    posts_list = Post.objects.all().order_by("-date_posted")

    paginator = Paginator(posts_list,5)
    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)

    context = {
        'posts': posts
    }
    return render(request, 'home.html', context)

def user_home(request, username):
    user = get_object_or_404(User, username=username)
    posts_list = Post.objects.filter(author=user).order_by("-date_posted")

    paginator = Paginator(posts_list, 5)
    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)

    context = {
        'posts': posts,
        'user': user,
        'post_count': posts_list.count()
    }
    return render(request, 'user_home.html', context)

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

@login_required
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
        else:
            return render(
                request,
                'create.html',
                {'form': form}
            )
    
    return render(
        request,
        'create.html',
        {'form': form}
    )

@login_required
def update(request , pk):
    post = Post.objects.get(pk = pk)
    if post.author != request.user:
        messages.error(request, "You are not allowed to edit someone else's post.BRUH!")
        return redirect('web-home')
    
    if request.method == "GET":
        form = PostForm(instance=post)
    else:
        form = PostForm(request.POST , instance= post)
        if form.is_valid():
            post = form.save()
            messages.success(request, 'The post has been updated successfully')
            return redirect('web-detail' ,post.pk)
        else:
            return render(
                request,
                'create.html',
                {'form': form, 'post': post}
                )
    
    return render(
        request,
        'create.html',
        {'form': form , 'post': post}
    )

@login_required
def delete(request , pk):
    post = Post.objects.get(pk = pk)
    if post.author != request.user:
        messages.error(request,"You can't delete someone else's post. BRUH !")
        return redirect('web-home')
    post.delete()
    messages.success(request, "Post Deleted Successfully!")
    return redirect('web-home')