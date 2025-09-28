from django.urls import path
from . import views

urlpatterns = [
    path("", views.api_home, name="api_home"),
    path("blogs", views.blog_posts, name="blogs"),
    path("blogs/<str:slug>", views.BlogDetail, name="blog_detail")
]