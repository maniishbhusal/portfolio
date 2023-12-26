from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('blogs/', views.blogs_page, name='blogs_page'),
    path('blogs/<slug:slug>/', views.detailed_blog, name='detailed_blog'),
    path('blogs/update/<slug:slug>/', views.update_blog, name='update_blog'),
    path('blogs/delete/<slug:slug>/', views.delete_blog, name='delete_blog'),
    path('contact/', views.contact, name='contact'),
    path('signup/',views.signup,name='signup'),
    path('login/',views.user_login,name='user_login'),
    path('logout/',views.user_logout,name='user_logout'),

    # API to post a comment
    path('post-comment/', views.post_comment, name='post_comment')
]