from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from accounts.models import Profile


class Post(models.Model):

    user = models.ForeignKey(
        User, on_delete=models.CASCADE)
    image = models.ImageField(
        upload_to="images/")
    image2 = models.ImageField(upload_to="images/", blank=True)
    image3 = models.ImageField(upload_to="images/", blank=True)
    text = models.TextField()
    text2 = models.TextField(blank=True)
    text3 = models.TextField(blank=True)
    date = models.DateTimeField(null=True, auto_now_add=True)
    title = models.CharField(max_length=250)
    #address = models.CharField(max_length=250)
    email = models.EmailField()
    #price = models.CharField(max_length=250, default="Dogovor")

    def summary(self):
        return self.text[:200]

    def pub_date_pretty(self):
        return self.date.strftime("%b %e %Y")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("detail", kwargs={"pk": self.pk})

    
