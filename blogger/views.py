# project_root/blogger/views.py (the app's views.py)

from django.shortcuts import render, get_object_or_404
from .models import Post
from django.http import Http404 # Already there but ensure it is


# Existing post_list and post_detail views (keep them as they are)
def post_list(request):
    posts = Post.published.all()
    context = {
        'posts': posts,
        'page_title': 'Latest Blog Posts'
    }
    return render(request, 'blogger/post_list.html', context)


def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post,
                             status=Post.Status.PUBLISHED,
                             publish__year=year,
                             publish__month=month,
                             publish__day=day,
                             slug=post)
    context = {
        'post': post,
        'page_title': post.title
    }
    return render(request, 'blogger/post_detail.html', context)


def post_archive_year(request, year):
    """
    Displays a list of all published blog posts for a particular year.
    Will show 'No posts found' if queryset is empty.
    """
    posts = Post.published.filter(publish__year=year)

    context = {
        'posts': posts,
        'page_title': f"Blog Posts from {year}"
    }
    return render(request, 'blogger/post_list.html', context)


def post_archive_month(request, year, month):
    """
    Displays a list of all published blog posts for a particular month and year.
    Will show 'No posts found' if queryset is empty or month is invalid.
    """
    month_name = ''
    try:
        import datetime
        month_name = datetime.date(year, month, 1).strftime('%B')
        # Check for valid month number, but let filter handle no posts
        if not (1 <= month <= 12):
             raise ValueError("Month must be between 1 and 12.")
    except ValueError:
        # If month is invalid, explicitly set a message or redirect to 404 if preferred
        # For showing 'No posts', we'll just set an informative title and an empty queryset
        posts = Post.objects.none() # Return an empty queryset
        context = {
            'posts': posts,
            'page_title': "Invalid Month for Archive"
        }
        return render(request, 'blogger/post_list.html', context)

    posts = Post.published.filter(publish__year=year, publish__month=month)

    context = {
        'posts': posts,
        'page_title': f"Blog Posts from {month_name} {year}"
    }
    return render(request, 'blogger/post_list.html', context)


def post_archive_day(request, year, month, day):
    """
    Displays a list of all published blog posts for a particular day.
    Will show 'No posts found' if queryset is empty or date is invalid.
    """
    date_obj = None
    try:
        import datetime
        date_obj = datetime.date(year, month, day)
    except ValueError:
        # If date is invalid, explicitly set a message or redirect to 404 if preferred
        posts = Post.objects.none() # Return an empty queryset
        context = {
            'posts': posts,
            'page_title': "Invalid Date for Archive"
        }
        return render(request, 'blogger/post_list.html', context)

    posts = Post.published.filter(publish__year=year, publish__month=month, publish__day=day)

    context = {
        'posts': posts,
        'page_title': f"Blog Posts from {date_obj.strftime('%B %d, %Y')}"
    }
    return render(request, 'blogger/post_list.html', context)