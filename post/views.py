from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import PostModel
from user.models import UserModel

def home(request):
    if request.method == 'GET':
        user = request.user.is_authenticated
        if user:
            context=dict()
            context['posts'] = PostModel.objects.all().order_by('-created_at')
            context['users'] = UserModel.objects.all()
            return render(request, 'post/post/home.html', context=context)
        return render(request, 'post/post/home.html')


@login_required(login_url='/signin/')
def post_create(request):
    if request.method == 'GET':
        return render(request, 'post/post/post_create.html')
    
    elif request.method == 'POST':
        user = request.user
        image = request.FILES['image']
        content = request.POST.get('content')
        PostModel.objects.create(author=user, image=image, content=content)
        return redirect('/')


def post_detail(request, post_id):
    if request.method == 'GET':
        context = dict()
        context['post'] = PostModel.objects.get(id=post_id)
        context['users'] = UserModel.objects.all()

        return render(request, 'post/post/post_detail.html', context=context)





        
