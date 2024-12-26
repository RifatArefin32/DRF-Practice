from django.urls import path
from .views import product_list_view, comment_list_view

urlpatterns = [
    path('list/', product_list_view, name='product_list'),
    path('comments/', comment_list_view, name='comment_list'),
]
