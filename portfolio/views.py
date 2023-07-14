from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Portfolio, Blog, Contact


# Create your views here.
def home(request):
    portfolio_lists = Portfolio.objects.all()[:3]
    blog_lists = Blog.objects.all().order_by('-created_at')[:3]
    context = {
        'portfolio_lists': portfolio_lists,
        'blog_lists': blog_lists,
    }

    return render(request, 'portfolio/home.html', context)


def about(request):
    return render(request, 'portfolio/about.html')


def portfolio(request):
    portfolio_lists = Portfolio.objects.all()
    context = {
        'portfolio_lists': portfolio_lists,
    }
    return render(request, 'portfolio/portfolio.html', context)


def blogs_page(request):
    blog_lists = Blog.objects.all().order_by('-created_at')
    context = {
        'blog_lists': blog_lists,
    }
    return render(request, 'portfolio/blogs_page.html', context)


def detailed_blog(request, slug):
    blog = Blog.objects.get(slug=slug)
    context = {
        'blog': blog,
    }
    return render(request, 'portfolio/detailed_blog.html', context)


def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']

        Contact.objects.create(name=name, email=email, message=message)
        messages.success(request, 'Your message has been sent successfully')
        return redirect('contact')

    return render(request, 'portfolio/contact.html')
