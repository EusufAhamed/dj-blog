from django.shortcuts import render, redirect
# from django.views import View

from user.forms import UserSignupForm
from user.models import User

# Create your views here.

def signinview(request):
    return render(request, 'auth/signin.html')

# def signupview(request):
#     return render(request, 'auth/signup.html')

# class Signup(View):
#     def get(self, req):
#         data = {}
#         template = 'auth/signup.html'

#         return render(req, template, data)

#     def post(self, req):
#         data = {}
#         data['form'] = UserSignupForm()
#         template = 'auth/signup.html'
#         # create a form instance and populate it with data from the request:
#         form = UserSignupForm(req.POST)

#         # check whether it's valid:
#         if form.is_valid():
#             # form.save()
#             username = form.cleaned_data.get('username')
#             email = form.cleaned_data.get('email')
#             password = form.cleaned_data.get('password')

#             User.objects.create_user(username=username, email=email, password=password)
#             # print(form.errors)
#             return redirect('user:signinview')

#         return render(req, template, data)

def signup(req):
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

            User.objects.create_user(username=username, email=email, password=password)

            return redirect('user:signinview')
    return render(req, template, data)

