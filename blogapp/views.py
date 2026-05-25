from django.shortcuts import render
from .models import Blog

# Create your views here.
def home(request):
    blogs = Blog.objects.all()
    return render(request, "index.html", {"blogs": blogs})

def read_blog(request,id):
    blog_data = Blog.objects.get(id=id)
    blog_data.views +=1
    blog_data.save()

    return render(request,"blog.html",{"blog":blog_data})