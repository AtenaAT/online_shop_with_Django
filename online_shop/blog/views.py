
from django.shortcuts import render
from django.http import HttpResponse
from .models import Post



# all post
def index(request):
    post_list= Post.objects.all().order_by('post_published')

    context={
        'post_list':post_list,
    }
    return render(request,"index.html", context)

# each post in detailed
def detail(request, post_id):

    post= Post.objects.get(pk= post_id)
    context={
        'post':post,
    }
    
    return render(request, 'detail.html',context)
