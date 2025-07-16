from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="Home"),
    path('blogs/', include('blogger.urls',namespace='blogger')),
    path('challenges/', include('challenges.urls',namespace='challenges')),
]

# path('', RedirectView.as_view(url='/challenges/', permanent=True)),
