from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post, Project
from .forms import PostForm, ProjectForm

import random

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts' : posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post' : post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(data=request.POST, files=request.FILES,)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, files=request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})   

def project_list(request):
    projects = Project.objects.all()
    return render(request, 'blog/project_list.html', {'projects' : projects})

def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    return render(request, 'blog/project_detail.html', {'project' : project})

def project_edit(request, pk):
    project = Project.objects.get(pk=pk)
    if request.method == "POST":
        form = ProjectForm(request.POST, files=request.FILES, instance=project)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('project_detail', pk=project.pk)
    else:
        form = ProjectForm(instance=project)
    return render(request, 'blog/project_edit.html', {'form': form}) 

def index(request):
    return render(request, 'blog/index.html')

def about(request):
    return render(request, 'blog/about.html')

def random_page(request):
    projects_number = len(Project.objects.all())
    selected_project = random.randint(1, projects_number)
    return redirect('project_detail', pk=selected_project)