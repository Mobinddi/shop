from django.urls import path

from .views import ProductListView, ProductDetailView, CommentCreateView, test_message


urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('comment/<int:product_id>', CommentCreateView.as_view(), name='comment_create'),
    path('message/', test_message)
]