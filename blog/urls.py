# blog/urls.py
from django.contrib.auth.views import LoginView,LogoutView
from django.urls import path
from . import views

urlpatterns = [
    path("", views.blog_index, name="blog_index"),
    path("post/<int:pk>/", views.blog_detail, name="blog_detail"),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path("category/<category>/", views.blog_category, name="blog_category"),
]