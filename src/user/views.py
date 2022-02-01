from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseForbidden

from user.forms import UserSignupForm, UserSigninForm, UserProfileUpdateForm
from user.models import User, Profile

# Create your views here.

def signin(req):
    # if user is already authenticate then the user can not see the login page
    if req.user.is_authenticated:
        return redirect('home')

    data = {}
    template = 'auth/signin.html'
    data['form'] = UserSigninForm(req.POST or None)

    if req.method == 'POST':
        if data['form'].is_valid():
            user = authenticate(
                email = data['form'].cleaned_data.get('email'), 
                password = data['form'].cleaned_data.get('password')
            )

            if user is not None:
                login(req, user)
                # if user is loged out by autometically and he wants to see her/him current page by login again
                if 'next' in req.POST:
                    return redirect(req.POST.get('next'))
                else:
                    return redirect('home')
            else:
                messages.warning(req, 'wrong credentials')
    return render(req, template, data)


def signup(req):
    # if user is already authenticate then the user can not see the login page
    if req.user.is_authenticated:
        return redirect('home')

    form = UserSignupForm(req.POST or None)
    data = {
        'form': form
    }
    template = 'auth/signup.html'

    if req.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            name = form.cleaned_data.get('name')

            user = User.objects.create_user(username=username, email=email, password=password)
            # when a user is created the Profile object also created
            Profile.objects.create(name=name, user_id=user.id)

            messages.success(req, 'registration successful')
            return redirect('user:signinview')

    return render(req, template, data)


@login_required(login_url='user:signinview')
def profile(req, username):
    data = {}
    data['userinfo'] = User.objects.get(username=username)
    template = 'profile/profile.html'

    return render(req, template, data)

@login_required(login_url='user:signinview')
def profile_update(req, username):
    data = {}
    template = 'profile/profile_update.html'
    data['userinfo'] = User.objects.get(username=username)
    data['form'] = UserProfileUpdateForm(req.POST or None, req.FILES or None)
    
    # a user can not see othere user setting page
    if req.user.id != data['userinfo'].id:
        return HttpResponseForbidden('you are restricted to access this page')
    
    if req.method == 'POST':
        if data['form'].is_valid():
            data['userinfo'].profile.name = data['form'].cleaned_data.get('name')
            data['userinfo'].profile.about = data['form'].cleaned_data.get('about')

            if data['form'].cleaned_data.get('profile_image'):
                data['userinfo'].profile.profile_image = data['form'].cleaned_data.get('profile_image')
            else:
                data['userinfo'].profile.profile_image = data['userinfo'].profile.profile_image

            if data['form'].cleaned_data.get('cover_image'):
                data['userinfo'].profile.cover_image = data['form'].cleaned_data.get('cover_image')
            else:
                data['userinfo'].profile.cover_image = data['userinfo'].profile.cover_image
                
            data['userinfo'].profile.facebook = data['form'].cleaned_data.get('facebook')
            data['userinfo'].profile.twitter = data['form'].cleaned_data.get('twitter')
            data['userinfo'].profile.google_plus = data['form'].cleaned_data.get('google_plus')
            data['userinfo'].profile.instagram = data['form'].cleaned_data.get('instagram')
            data['userinfo'].profile.save()

            messages.success(req, 'profile has been updated successfully')
            return redirect('user:profileUpdateView', username)

    return render(req, template, data)


def loginout(req):
    logout(req)
    return redirect('home')