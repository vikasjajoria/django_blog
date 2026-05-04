from django.urls import path
from . import views


urlpatterns = [
    path('search/', views.search, name='search'),   
    path('<slug:slug>/', views.blogs, name='blogs'),
    path('category/<int:category_id>/', views.posts_by_category, name='posts_by_category')
]