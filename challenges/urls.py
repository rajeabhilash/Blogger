from django.urls import path
from . import views

app_name = 'challenges'

urlpatterns = [
    path('', views.index,name='index'),
    path('<int:month_number>', views.month_number_challenge, name='month_number_challenge'),
    path('<str:month_name>', views.month_name_challenge, name='month_name_challenge'),
]