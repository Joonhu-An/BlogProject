from django.shortcuts import render
from .models import BlogFrame

def main(request):
    blogs = BlogFrame.objects
    return render(request, 'main.html', {'blogs':blogs})
