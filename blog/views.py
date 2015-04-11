from django.shortcuts import render, get_object_or_404, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from blog.forms import UserForm,PostForm
from django.template import RequestContext
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from blog.s3 import post as s3_post
from blog.s3 import get as s3_get
import os.path
from blog.models import Post, Comment

def index(request):
  context = RequestContext(request)
  return render_to_response('blog/index.html',context_instance=context)


def register(request):
  context = RequestContext(request)
  registered = False
  if request.method == 'POST':
    user_form = UserForm(data=request.POST)
    if user_form.is_valid():
      user = user_form.save()
      user.set_password(user.password)
      user.save()

      registered = True
    else:
      print user_form.error
  else:
    user_form = UserForm()

  return render_to_response(
          'blog/register.html', 
          {'user_form': user_form, 'registered': registered}, 
          context)


def user_login(request):
  context = RequestContext(request)

  if request.method=='POST':
    username = request.POST['username']
    password = request.POST['password']

    user = authenticate(username=username, password=password)

    if user is not None:
      if user.is_active:
        login(request, user)
        return HttpResponseRedirect('/blog/')
      else:
        return HttpResponse('Your account is disabled.')
    else:
      print 'invalid login details: {0}, {1}.'.format(username, password)
      return HttpResponse('invalid login details supplied.')

  else:
    return render_to_response('blog/login.html', {}, context)

@login_required
def user_logout(request):
  logout(request)
  return HttpResponseRedirect('/blog/')

@login_required
def add_post(request):
  context = RequestContext(request)

  if request.method == 'POST':
    post_form = PostForm(data=request.POST)
    if post_form.is_valid():
      image = request.FILES['image']
      name, ext = os.path.splitext(image.name)
      post = post_form.save(commit=False)
      post.image_path = s3_post(request.user.id, image, ext)
      post.user = request.user
      post.save()
    else:
      print post_form.errors
    return HttpResponseRedirect(reverse('post_detail', args=(post.id,)))
  else:
    post_form = PostForm()
    return render_to_response('blog/add_post.html', {'post_form': post_form,}, context)
    
@login_required
def list_post(request):
  context = RequestContext(request)
  latest_post_list = Post.objects.order_by('-pub_date')[:5]
  return render_to_response('blog/list_post.html', {'latest_post_list': latest_post_list,}, context)

@login_required
def post_detail(request, post_id):
  context = RequestContext(request)
  if request.method == 'GET':
    try:
      post = Post.objects.get(pk=post_id)
    except Poll.DoesNotExist:
      raise Http404
    post_comment = Comment.objects.filter(post_id=post_id)
    return render_to_response('blog/post_detail.html', { 'post': post, 'post_comment': post_comment, 'post_id': post_id}, context)
  else:
    try:
      post = Post.objects.get(pk=post_id)
    except Poll.DoesNotExist:
      raise Http404
    comment = Comment()
    comment.content = request.POST['content']
    comment.user = request.user
    comment.post = post
    comment.save()
    return HttpResponseRedirect(reverse('post_detail', args=(post_id,)))
# Create your views here.
