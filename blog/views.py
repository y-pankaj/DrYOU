from django.utils import timezone
from .models import Post
from .forms import PostForm
from django.shortcuts import render, get_object_or_404 , redirect


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post_detail.html', {'post': post})


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user

            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'post_edit.html', {'form': form})


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        print(form.errors)
        if form.is_valid():
            data = form.cleaned_data['text']
            post = form.save(commit=False)
            #data = post.cleaned_data['text']
            if len(data) < 150:
                x = data + '...'
            else:
                x = data[:140] + '.....'

            post.snippet = x
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'post_edit.html', {'form': form})


def post_all(request):
    posts = Post.objects.all()
    return render(request, 'post_all.html', {'posts': posts})


def testview(request):
    return render(request, 'blog-home.html', {'posts': Post.objects.all()})
