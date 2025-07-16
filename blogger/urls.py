# project_root/blogger/urls.py (the app's urls.py)

from django.urls import path, re_path # Import re_path for flexibility, though not strictly needed here
from . import views

app_name = 'blogger'

urlpatterns = [
    # 1. Post list view (all posts) - will now be at /posts/
    path('', views.post_list, name='post_list'),

    # 2. Post detail view (most specific) - /posts/YYYY/MM/DD/slug/
    path('<int:year>/<int:month>/<int:day>/<slug:post>/',
         views.post_detail,
         name='post_detail'),

    # 3. Posts by day - /posts/YYYY/MM/DD/
    path('<int:year>/<int:month>/<int:day>/',
         views.post_archive_day, # <--- NEW VIEW
         name='post_archive_day'),

    # 4. Posts by month - /posts/YYYY/MM/
    path('<int:year>/<int:month>/',
         views.post_archive_month, # <--- NEW VIEW
         name='post_archive_month'),

    # 5. Posts by year - /posts/YYYY/
    path('<int:year>/',
         views.post_archive_year, # <--- NEW VIEW
         name='post_archive_year'),
]