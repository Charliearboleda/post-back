from django.urls import path
from . import views

urlpatterns = [
    path('api/comments', views.CommentList.as_view(), name='comment_list'),
    path('api/comments/<int:pk>', views.CommentDetail.as_view(), name='comment_detail'),
]
