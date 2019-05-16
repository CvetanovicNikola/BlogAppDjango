
from django.urls import path
# rom . import views
from .views import Post_detail, All_posts, CreatePost, AllUserPosts, UpdatePost, DeletePost, upvote, downvote


urlpatterns = [


    path("", All_posts.as_view(), name="allposts"),
    path("<int:pk>/", Post_detail.as_view(), name="detail"),
    path("user/<str:user>", AllUserPosts.as_view(), name="all_user_posts"),
    path("post/new/", CreatePost.as_view(), name="create_post"),
    path("<int:pk>/update", UpdatePost.as_view(), name="update_post"),
    path("<int:pk>/delete", DeletePost.as_view(), name="delete_post"),
    path("<int:pk>/<username>/upvote", upvote, name="upvote"),
    path("<int:pk>/<username>/downvote", downvote, name="downvote")


]
