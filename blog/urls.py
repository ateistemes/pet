# blog/urls.py

from django.urls import path
from . import views
from .views import register, CustomLoginView, CustomLogoutView, profile_view
urlpatterns = [
    path("", views.blog_index, name="blog_index"),
    path("post/<int:pk>/", views.blog_detail, name="blog_detail"),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('register/', register, name='register'),
    path('accounts/profile/', profile_view, name='profile'),
    path("category/<category>/", views.blog_category, name="blog_category"),
]