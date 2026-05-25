from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Blog(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.TextField()
    body = models.TextField()
    writer = models.ForeignKey(User,on_delete=models.CASCADE)
    views = models.IntegerField()


    def __str__(self) -> str:
        return self.title