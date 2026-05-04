from django.shortcuts import render
from blogs.models import Blog, Category
from assignments.models import About


def home(request):
    featured_posts = Blog.objects.filter(is_featured=True).order_by('-updated_at')
    normal_posts = Blog.objects.filter(is_featured=False).order_by('-created_at')

    # Fetch about us
    try:
        about = About.objects.get()
    except:    
        about = None



    context = {
        'featured_posts': featured_posts,
        'posts': normal_posts,
        'about': about,
    }
    return render(request, 'home.html', context)
    
