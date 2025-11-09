from django.urls import path
from .views import (HomePageView, AboutPage2View, BlogListView,
                    BlogDetailView, BlogCreateView, BlogUpdateView,
                    BlogDeleteView)

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPage2View.as_view(), name='about'),
    path('blog/', BlogListView.as_view(), name='blogs'),
    path('blog/<int:pk>/', BlogDetailView.as_view(), name='blog-detail'),
    path('blog/create', BlogCreateView.as_view(), name='blog-create'),
    path('blog/<int:pk>/edit', BlogUpdateView.as_view(), name='blog-update'),
    path('blog/<int:pk>/delete', BlogDeleteView.as_view(), name='blog-delete'),
]