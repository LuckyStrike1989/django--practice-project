from django.urls import path
from . import views

#from blog.views import post_list, post_detail, post_add

urlpatterns = [
    path("", views.index, name='index'),
    path("feeds/", views.feeds, name="feeds")
]