from django.shortcuts import render
from blog.models import Post    # Post 모델을 사용하기 위해 import

# Create your views here.
def post_list(request):
    # 모든 Post 객체를 가진 QuerySet
    posts = Post.objects.all()

    context = {
        "posts": posts,
    }

    return render(request, "post_list.html", context)