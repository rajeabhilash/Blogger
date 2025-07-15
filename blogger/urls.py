from django.urls import path
from . import views

urlpatterns = [
    path('', views.pratham, name='FirstBlog'),
]