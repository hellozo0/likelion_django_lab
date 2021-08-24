from django.db import reset_queries
from django.shortcuts import render, get_object_or_404, redirect
from .forms import CommentForm
from postcrud.models import Post
from commentcrud.models import Comment

# Create your views here.
def commentcreate(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method=='POST' :
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit = False)
            comment.post = post
            comment.save()
            return redirect('postshow', post_id=post.pk)
        else:
            redirect('list')
    else:
        form = CommentForm()
        return render(request, 'postshow.html',{'form' : form, 'post': post})
    

#https://korinkorin.tistory.com/31

def commentedit(request,comment_id, post_id):
    comment = Comment.objects.get(id=comment_id)
    form = CommentForm(instance=comment)
    if request.method=='POST' :
        form = CommentForm(request.POST, instance=comment) # 구글링 --> form --> update_form
        if form.is_valid():  # 구글링 --> form --> update_form 
            comment.save() # 구글링 --> comment --> update_form
            return r('postshow', post.id)
        return render(request, 'edit.html', {'form':form})
    

def commentdelete(request,comment_id, post_id):
    comment = Comment.objects.get(id=comment_id)
    comment.delete() #문제의 구간..?
    return redirect('postshow')


