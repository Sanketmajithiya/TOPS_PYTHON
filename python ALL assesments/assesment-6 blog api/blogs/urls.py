from django.urls import path
from .views import BlogListAPI, BlogDetailAPI  

urlpatterns = [
    path('', BlogListAPI, name='BlogListAPI'),
    path('BookDetailAPI/<int:blog_id>/', BlogDetailAPI, name='BookDetailAPI'),  
]
