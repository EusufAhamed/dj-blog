from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from post.models import Post
from post.forms import AddPostForm, UpdatePostForm
from utils.slug import slugify

# Create your views here.

@login_required(login_url='user:signinview')
def add(req):
    data = {}
    # in the view, category came from utils.context_processors.context_data 
    data['form'] = AddPostForm(req.POST or None, req.FILES or None)
    template = 'add.html'

    if req.method == 'POST':
        if data['form'].is_valid():
            title = data['form'].cleaned_data.get('title')
            slug = slugify(title)
            image = data['form'].cleaned_data.get('image')
            description = data['form'].cleaned_data.get('description')
            user_id = req.user.id
            category_id = data['form'].cleaned_data.get('category')

            Post.objects.create(
                title=title,
                slug=slug,
                category_id=category_id,
                user_id=user_id,
                image=image,
                description=description
            )
            messages.success(req, 'post has been created')
            return redirect('user:profileview', req.user.username)

    return render(req, template, data)

def details(req, post_slug):
    data = {}
    data['post'] = Post.objects.get(slug=post_slug)
    data['page_title'] = data['post'].title
    template = 'details.html'

    return render(req, template, data)

@login_required(login_url='user:signinview')
def edit(req, post_id):
    data = {}
    data['postinfo'] = Post.objects.get(id=post_id)
    data['form'] = UpdatePostForm(req.POST or None, req.FILES or None)
    template = 'edit.html'

    # a user can not see other user post edit page
    if req.user.id != data['postinfo'].user.id:
        return render(req, '404.html', {'error': 'you are restricted to access this page'})

    if req.method == 'POST':
        if data['form'].is_valid():
            data['postinfo'].title = data['form'].cleaned_data['title']
            data['postinfo'].description = data['form'].cleaned_data['description']
            data['postinfo'].slug = slugify(data['postinfo'].title)

            if data['form'].cleaned_data['image']:
                data['postinfo'].image = data['form'].cleaned_data['image']
            else:
                data['postinfo'].image
            data['postinfo'].category_id = data['form'].cleaned_data['category']
            data['postinfo'].save()

            messages.success(req, 'post updated successfully')
            return redirect('user:profileview', req.user.username)


    return render(req, template, data)