from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to="images",
                              default="profile_default.jpg")
    date = models.DateTimeField(null=True, auto_now_add=True)

    upVotes = models.IntegerField(default=0)
    downVotes = models.IntegerField(default=0)
    voted = models.TextField(blank=True)

    def __str__(self):
        return f"{self.user.username} Profile"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.photo.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.photo.path)

    def rating(self):
        return (self.upVotes + self.downVotes / 2)
