from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm

from . models import Blog_post

class BlogForm(ModelForm):
    class Meta:
        model = Blog_post
        fields = ['title', 'author', 'body']

def post_list(request):
    post = Blog_post.objects.all()
    data = {}
    data['object_list'] = post
    print(post)
    return render(request, 'blogpost/post_list.html', data)

def post_view(request, pk):
    post= get_object_or_404(Blog_post, pk=pk)
    return render(request, 'blogpost/post_detail.html', {'object':post})

def post_create(request):
    form = BlogForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('post_list')
    return render(request, 'blogpost/post_form.html', {'form':form})

def post_update(request, pk):
    post= get_object_or_404(Blog_post, pk=pk)
    form = BlogForm(request.POST or None, instance=post)
    if form.is_valid():
        form.save()
        return redirect('post_list')
    return render(request, 'blogpost/post_form.html', {'form':form})

def post_delete(request, pk):
    post = get_object_or_404(Blog_post, pk=pk)
    if request.method=='POST':
        post.delete()
        return redirect('post_list')
    return render(request, 'blogpost/post_delete.html', {'object':post})

