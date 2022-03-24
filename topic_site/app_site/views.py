from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .forms import TopicForm, EditTopicDescriptionForm, PostForm, LoginForm, RegisterForm
from .models import Topic, Post


@login_required
def add_topic(request):
    if request.method == 'POST':
        form = TopicForm(request.POST)
        if form.is_valid():
            topic = Topic.objects.create(**form.cleaned_data)
            return redirect('topic_detail', topic.id)
    else:
        form = TopicForm()
        return render(request, 'form.html', {'form': form})


@login_required
def edit_topic(request, topic_id):
    if request.method == 'POST':
        form = EditTopicDescriptionForm(request.POST)
        if form.is_valid():
            topic = get_object_or_404(Topic, pk=topic_id)
            topic.description = form.cleaned_data["description"]
            topic.save()
            return redirect('topic_detail', topic.id)
    else:
        form = EditTopicDescriptionForm()
        return render(request, 'form.html', {'form': form})


@login_required
def add_post(request, topic_id):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            user = request.user
            topic = get_object_or_404(Topic, pk=topic_id)
            Post.objects.create(topic=topic, user=user, **form.cleaned_data)
            return redirect('topic_post_list', topic.id)
    else:
        form = PostForm()
        return render(request, 'form.html', {'form': form})


@login_required
def delete_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    user = request.user
    if post.user == user:
        post.delete()
        return redirect('topic_post_list', post.topic.id)
    return HttpResponse('You can delete only your post!')


@login_required
def edit_post(request, post_id):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            user = request.user
            post = get_object_or_404(Post, pk=post_id)
            if post.user == user:
                post.text = form.cleaned_data["text"]
                post.save()
                return redirect('topic_post_list', post.topic.id)
            return HttpResponse('You can edit only your post!')
    else:
        form = PostForm()
        return render(request, 'form.html', {'form': form})


def index(request):
    return render(request, 'index.html')


def topic_detail(request, topic_id):
    topic = get_object_or_404(Topic, pk=topic_id)
    return render(request, 'topic_detail.html', {'topic': topic})


def topic_list(request):
    topics = Topic.objects.all()

    return render(request, 'topic_list.html', {'topics': topics})


def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'post_detail.html', {'post': post})


def post_list(request):
    posts = Post.objects.all()
    return render(request, 'post_list.html', {'posts': posts})


def topic_post_list(request, topic_id):
    posts = Post.objects.filter(topic=topic_id)
    return render(request, 'post_list.html', {'posts': posts})


def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect("index")
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'form.html', {'form': form})


def logout_user(request):
    logout(request)
    return redirect("index")


def register_user(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            User.objects.create_user(**form.cleaned_data)
            return redirect("login_user")
        else:
            return HttpResponse('Invalid registration')
    else:
        form = RegisterForm()

        return render(request, "form.html", {"form": form})


