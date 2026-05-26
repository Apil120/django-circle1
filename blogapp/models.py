from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Blog(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.TextField()
    body = models.TextField()
    writer = models.ForeignKey(User,on_delete=models.CASCADE)
    views = models.IntegerField()
    image_path = models.ImageField(upload_to="images/", blank=True)
    video_path = models.FileField(upload_to="videos/", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self) -> str:
        return self.title