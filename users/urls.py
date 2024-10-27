from django.urls import path
from . import views

#from blog.views import post_list, post_detail, post_add

urlpatterns = [
    path("", views.login_view, name='login_view'),
    path("login", views.login_view, name='login_view'),
]