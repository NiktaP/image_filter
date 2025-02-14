from django.urls import path
from .views import gray_filter
urlpatterns = [
    path('gray_filter/', gray_filter, name='gray_filter'),
]