from django.urls import path
from . import views

urlpatterns = [
    path('commentcreate/<int:post_id>', views.commentcreate, name='commentcreate'),
    path('commentedit/<int:comment_id>/<int:post_id>', views.commentedit, name='commentedit'),
    path('commentdelete/<int:comment_id>/<int:post_id>', views.commentdelete, name='commentdelete'),
]