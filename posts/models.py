from django.db import models
# from django.forms import CharField, DateTimeField
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=10485760)
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    posted_at = models.DateTimeField(default=datetime.now, blank=True)
    post_image = models.ImageField(null=True, blank=True, upload_to="images/")

    def __str__(self):
        return self.title
