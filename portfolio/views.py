from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'portfolio/home.html')

def about(request):
    return render(request,'portfolio/about.html')

def portfolio(request):
    return render(request,'portfolio/portfolio.html')

def blogs_page(request):
    return render(request,'portfolio/blogs_page.html')