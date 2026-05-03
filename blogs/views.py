from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog, Category

# Create your views here.
def posts_by_category(request, category_id):
    # fatch the post that belongs to the category with the id category_id
    posts = Blog.objects.filter(status=1, category=category_id)
    try:
        category = Category.objects.get(pk=category_id)
    except:
        return redirect('home')
            
    context = {
        'posts': posts,
        'category': category,
    }
    return render(request, 'posts_by_category.html', context)