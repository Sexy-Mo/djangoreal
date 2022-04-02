from django.shortcuts import render,get_object_or_404,redirect
from blog.models import Post,Comment
from django.utils import timezone
from django.views.generic import (TemplateView,ListView,CreateView,UpdateView,DeleteView,DetailView)
from django.urls import reverse_lazy,reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from blog.forms import PostForm,CommentForm,UserForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import login,logout,authenticate



# Create your views here.
class aboutview (TemplateView):
    template_name='about.html'

class postlistview(ListView):
    model=Post
    def get_queryset (self):
        return Post.objects.order_by('-create_date')

class postdetailview (DetailView):
    model=Post

class createpostview (LoginRequiredMixin,CreateView):
    login_url='/login/'#here
    redirect_field_name="blog/post_detail.html"#here
    form_class=PostForm#here
    model=Post

class updatepostview (LoginRequiredMixin,UpdateView):
    login_url='/login/'
    redirect_field_name="blog/post_detail.html"
    form_class=PostForm
    model=Post

class deletepostview (LoginRequiredMixin,DeleteView):
    model=Post
    success_url=reverse_lazy('postlist')

class draftlistview (LoginRequiredMixin,ListView):
          login_url='/login/'
          redirect_field_name="blog/post_list.html"
          model=Post
          def get_queryset(self):
              return Post.objects.filter(publish_date__isnull=True).order_by('create_date')


######################################################################
@login_required
def add_comment_to_post (request,pk):
    post=get_object_or_404 (Post,pk=pk)
    if request.method=='POST':
        form=CommentForm(request.POST)
        if form.is_valid():
            comment=form.save(commit=False)
            comment.post=post
            comment.save()
        return redirect ('postdetail',pk=comment.post.pk)
    else:
        form=CommentForm()
    return render (request,'blog/comment_form.html',{'form':form})

@login_required
def comment_approve(request,pk):
    comment=get_object_or_404(Comment,pk=pk)
    comment.approve()
    return redirect ('postdetail',pk=comment.post.pk)

@login_required
def comment_remove (request,pk):
    comment =get_object_or_404(Comment,pk=pk)
    post_pk=comment.post.pk
    comment.delete()
    return redirect ('postdetail',pk=post_pk)

@login_required
def post_publish (request,pk):
    post =get_object_or_404(Post,pk=pk)
    post.publish()
    return redirect ('postdetail',pk=pk)

    #################################################################


def register(request):
    registered=False
    if request.method=='POST':
        userformobject=UserForm(data=request.POST)
        if userformobject.is_valid() :
            pozer=userformobject.save()
            pozer.set_password(pozer.password)
            pozer.save()
            registered=True
        else:
            print(userformobject.errors)
    else:
        userformobject=UserForm()


    dict={'registeredkey':registered ,'userformobjectkey':userformobject }
    return render(request,'blog/register.html',dict)


# Create your views here.
