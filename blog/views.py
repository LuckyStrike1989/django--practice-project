from django.shortcuts import render, redirect
from blog.models import Post    # Post 모델을 사용하기 위해 import
from blog.models import Comment

# Create your views here.
def post_list(request):
    # 모든 Post 객체를 가진 QuerySet
    posts = Post.objects.all()

    context = {
        "posts": posts,
    }

    return render(request, "blog/post_list.html", context)

def post_detail(request, post_id):
    post = Post.objects.get(id=post_id)

    if request.method == "POST":
        comment_content = request.POST["comment"]
        # 전달된 "comment"의 값으로 Comment 객체를 생성한다.
        Comment.objects.create(
            post=post,
            content=comment_content,
        )
    
    # 1. GET 요청으로 글 상세 페이지를 보여주거나
    # 2. POST 요청으로 댓글이 생성되거나
    # 두 경우 모두, 이 글의 상세 페이지를 보여주면 된다.

    context = {
        "post" : post
    }

    return render(request, "blog/post_detail.html", context)

def post_add(request):
    if request.method == "POST":
        print("method POST")
        title = request.POST["title"]
        content = request.POST["content"]
        thumbnail = request.FILES["thumbnail"]  # 이미지 파일
        
        post = Post.objects.create(
            title=title,
            content=content,
            thumbnail=thumbnail,
        )
        return redirect(f"/posts/{post.id}/")
    else:
        print("method GET")
    
    return render(request, "blog/post_add.html")