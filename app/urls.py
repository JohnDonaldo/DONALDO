from django.urls import path
from .views import HomePageView, AboutPage2View

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPage2View.as_view(), name='about'),
]