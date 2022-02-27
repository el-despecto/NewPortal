from django.urls import path
from .views import PostList, PostDetailView, PostCreateView, PostDeleteView, PostUpdateView, PostSearch

urlpatterns = [
    path('', PostList.as_view()),
    path('news_search/', PostSearch.as_view(), name='news_search'),
    path('<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('create/', PostCreateView.as_view(), name='post_create'),
    path('create/<int:pk>', PostUpdateView.as_view(), name='post_update'),
    path('delete/<int:pk>', PostDeleteView.as_view(), name='post_delete'),
]