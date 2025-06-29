from django.urls import path
from . import views

urlpatterns = [
    path("posts/", views.PostListCreateView.as_view(), name="post-list-create"),
    path("posts/<slug:slug>/", views.PostDetailView.as_view(), name="post-detail"),
    path("categories/", views.CategoryListView.as_view(), name="category-list"),
    path("featured/", views.featured_posts, name="featured-posts"),
]
