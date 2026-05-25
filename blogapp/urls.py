from django.urls import path
from .views import home,read_blog

urlpatterns = [
    path("",home),
    path("blog/<int:id>/",read_blog)
]
