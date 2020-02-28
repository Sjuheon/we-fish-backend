from django.urls import path
from .views      import CategoryView, ProductListView, ProductView, ThemeView, ReviewView

urlpatterns = [
    path('/category_list', CategoryView.as_view()),
    path('/product_list', ProductListView.as_view()),
    path('/product_info', ProductView.as_view()),
    path('/theme', ThemeView.as_view()),
    path('/review', ReviewView.as_view()),
]
