from django.urls import path
from . import views

#from blog.views import post_list, post_detail, post_add

urlpatterns = [
    path("", views.post_list, name='post_list'),
    path("posts/", views.post_list, name='post_list'),
    path("posts/<int:post_id>/", views.post_detail, name='post_detail'),
    path("posts/add/", views.post_add, name='post_add'),
]