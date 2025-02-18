from django.urls import path
from .views import gray_filter,blur_filter
urlpatterns = [
    path('gray_filter/', gray_filter, name='gray_filter'),
    path('blur_filter/',blur_filter, name='blur_filter')
]