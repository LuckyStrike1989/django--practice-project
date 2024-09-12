"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from config.views import main
from config.views import burger_list
from config.views import burger_search
from config.views import index
from blog.views import post_list, post_detail, post_add

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", index),
    path("posts/", post_list),
    path("posts/<int:post_id>/", post_detail),
    path("posts/add/", post_add),

    path("main/", main),
    path("burgers/", burger_list),
    path("search/", burger_search),
]

urlpatterns += static(
    #URL의 접두어가 MEDIA_URL일 때는 정적파일을 돌려준다
    prefix = settings.MEDIA_URL,
    #돌려줄 디렉터리는 media_root를 기준으로 한다
    document_root = settings.MEDIA_ROOT,
)