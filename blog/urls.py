from django.urls import path
from .views import ArticlesPost,ArticleAPIView,CategoryAPIView,CategoriesPost

urlpatterns = [
    path('<int:pk>/',ArticlesPost.as_view(),name='blog-home'),
    path('',ArticleAPIView.as_view(),name='blog-list-article'),
    path('category/<int:pk>/',CategoriesPost.as_view(),name='category-home'),
    path('category/',CategoryAPIView.as_view(),name='blog-list-category'),
]