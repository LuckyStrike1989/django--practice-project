from django.http import HttpResponse
from django.shortcuts import render
from burgers.models import Burger

def main(request):
    return render(request, "main.html")
    #return HttpResponse("안녕하세요, Python")
    
def burger_list(request):
    burgers = Burger.objects.all()
    print("전체 햄버거 목록:", burgers)

    context = {
        "burgers" : burgers
    }

    return render(request, "burger_list.html", context)
    #return HttpResponse("pyburger의 햄버거 목록입니다")

def burger_search(request):
    print("request ::: ", request)

    keyword = request.GET.get("keyword")
    print("keyword ::: ", keyword)

    burgers = Burger.objects.filter(name__contains=keyword)
    print("burgers ::: ", burgers)

    context = {
        "burgers" : burgers
    }

    return render(request, "burger_search.html", context)