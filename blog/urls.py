from django.urls import path
from . import views
from .views import blog

urlpatterns = [
    path('', views.blog, name="blog"),
    path('blog/', blog, name='blog'),
]