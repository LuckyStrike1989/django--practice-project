from django.shortcuts import render, redirect

def index(request):
    return render(request, "posts/index.html")

def feeds(request):
    # 요청(request)으로부터 사용자 정보를 가져온다
    #user = request.user

    # 가져온 사용자가 '로그인 했는지' 여부를 가져온다.
    #is_authenticated = user.is_authenticated

    if not request.user.is_authenticated:
        return redirect("/users/login")

    return render(request, "posts/feeds.html")