from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from .forms import CreateUserForm
from django.contrib.auth import authenticate, login, logout
from .models import *
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def home(request, category_slug=None):
    category_page = None
    post_list = None
    if category_slug is not None:
        category_page = get_object_or_404(Category, slug=category_slug)
        post_list = Post.objects.filter(category=category_page)
    else:
        post_list = Post.objects.all().filter()

    return render(request, 'blog/home.html', {'category': category_page, 'post_list': post_list})


def article_detail(request, category_slug, post_slug):
    try:
        post_detail = Post.objects.get(category__slug=category_slug, slug=post_slug)
    except Exception as e:
        raise e
    return render(request, 'blog/detail_view.html', {'post_detail': post_detail})


def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for:' + user)
            return redirect('login')
    return render(request, 'blog/register.html', {'form': form})


def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Your username is incorrect')
    return render(request, 'blog/login.html')


def logoutUser(request):
    logout(request)
    return redirect('login')


def about(request):
    all_about = About.objects.all()
    return render(request, 'blog/about.html', {'all_about': all_about})