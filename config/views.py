from django.http import HttpResponse
from django.shortcuts import render, redirect
from burgers.models import Burger

def index(request):
    # 로그인되어 있는 경우, 피드 페이지로 redirect
    if request.user.is_authenticated:
        return redirect("/posts/feeds")
    else:
        return redirect("/users/login")
    #return render(request, "burger/index.html")

def main(request):
    return render(request, "burger/main.html")
    #return HttpResponse("안녕하세요, Python")
    
def burger_list(request):
    burgers = Burger.objects.all()
    print("전체 햄버거 목록:", burgers)

    context = {
        "burgers" : burgers
    }

    return render(request, "burger/burger_list.html", context)
    #return HttpResponse("pyburger의 햄버거 목록입니다")

def burger_search(request):
    keyword = request.GET.get("keyword")

    # keyword 값이 없을때 처리
    if keyword is not None:
        # keyword 값이 있을때 데이터 불러옴
        burgers = Burger.objects.filter(name__contains=keyword)
    else:
        # keyword 값이 없을때 []값으로 처리
        burgers = Burger.objects.none()
    
    context = {
        "burgers" : burgers
    }

    return render(request, "burger/burger_search.html", context)