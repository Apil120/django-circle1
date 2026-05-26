from django.urls import path
from .views import home,read_blog
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("",home),
    path("blog/<int:id>/",read_blog),
    path('login/', auth_views.LoginView.as_view(template_name='templates/login.html'), name='login'),
]
