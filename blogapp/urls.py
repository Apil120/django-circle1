from django.urls import path
from .views import home,read_blog
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("",auth_views.LoginView.as_view(template_name='templates/login.html'), name='login'),
    path("blog/<int:id>/",read_blog),
    path('home/',home ),
]
