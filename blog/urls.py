# blog/urls.py

from django.urls import path, include
from . import views

app_name = "blog"

urlpatterns = [
    path("", views.blog_index, name="dashboard"),
    path("post/<int:pk>/", views.blog_detail, name="detail"),
    path("category/<category>/", views.blog_category, name="category"),
]