from django.shortcuts import render, redirect
from .models import Post
from .forms import PostCreateForm, PostUpdateForm


def index_view(request):
    posts = Post.objects.all()

    return render(request, 'app/index.html', {'posts': posts})


def post_detail_view(request, pk):

    post = Post.objects.get(id=pk)

    if request.method == 'POST':
        form = PostUpdateForm(request.POST, request.FILES, instance=post)

        if form.is_valid():
            form.save()
    form = PostUpdateForm(instance=post)

    return render(request, 'app/post_detail.html', {'post': post, 'form': form})


def post_create_view(request):

    if request.method == 'POST':
        form = PostCreateForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('index')

    form = PostCreateForm()
    return render(request, 'app/post_create.html', {'form': form})


def post_delete_view(request, pk):

    post = Post.objects.get(id=pk)
    post.delete()
    return redirect('index')






