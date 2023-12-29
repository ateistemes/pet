# blog/urls.py

from django.urls import path, include
from . import views
from .views import register, MyLoginView, MyLogoutView

app_name = "blog"

urlpatterns = [
    path("", views.blog_index, name="blog_index"),
    path("post/<int:pk>/", views.blog_detail, name="blog_detail"),
    # path("accounts/", include("django.contrib.auth.urls")),
    path('login/', MyLoginView.as_view(), name='login'),
    path('logout/', MyLogoutView.as_view(), name='logout'),
    path('register/', register, name='register'),
    # path('accounts/profile/', profile_view, name='profile'),
    path("category/<category>/", views.blog_category, name="blog_category"),
]