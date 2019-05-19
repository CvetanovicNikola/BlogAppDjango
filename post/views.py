from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import F
from accounts.models import Profile

class All_posts(ListView):
    model = Post
    context_object_name = "posts"
    ordering = ["-date"]
    paginate_by = 3

    def get_queryset(self):

        try:
            title = self.request.GET.get('title')
        except:
            title = ""
        if title:
            objects_list = Post.objects.filter(title__icontains=title)
        else:
            objects_list = Post.objects.all()
        return objects_list


class Post_detail(DetailView):
    model = Post


class AllUserPosts(ListView):
    model = Post
    context_object_name = "posts"
    ordering = ["-date"]
    paginate_by = 3
    template_name = "post/user_posts.html"

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get("user"))
        return Post.objects.filter(user=user)


class CreatePost(LoginRequiredMixin, CreateView):
    model = Post
    readonly_fields = ("date")
    fields = [
        "title",  "email", "image", "text", "image2", "text2", "image3", "text3"
    ]
            #"address", "price",
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class UpdatePost(LoginRequiredMixin, UpdateView, UserPassesTestMixin):

    model = Post
    readonly_fields = ("date")
    fields = [
        "title",  "email", "image", "text", "image2", "text2", "image3", "text3"
    ]
            #"address", "price",
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.user:
            return True
        return False


class DeletePost(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = "/"

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.user:
            return True
        return False


class CF(F):
    ADD = '||'


@login_required
def upvote(request, pk, username):

    if request.method == "POST":
        post = get_object_or_404(Post, pk=pk)

        #print("mica" + coffeeshop.voted)
        if username in post.user.profile.voted:
            return redirect("/post" + "/" + str(post.id))
            
        else:
            if username not in post.user.profile.voted:
                pk=post.user.profile.id
                Profile.objects.filter(pk=pk).update(
                    voted="voted" + username)
            profile = get_object_or_404(Profile, pk=pk)
            profile.upVotes += 1
            profile.save()
            return redirect("/post" + "/" + str(post.id))


@login_required
def downvote(request, pk, username):
    if request.method == "POST":
        post = get_object_or_404(Post, pk=pk)

        if username in post.user.profile.voted:
            return redirect("/post" + "/" + str(post.id))
        else:
            if username not in post.user.profile.voted:
                pk=post.user.profile.id
                Profile.objects.filter(pk=pk).update(voted="voted" + username)
            profile = get_object_or_404(Profile, pk=pk)
            profile.downVotes += 1
            profile.save()
            return redirect("/post" + "/" + str(post.id))
