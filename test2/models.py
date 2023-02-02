from django.db import models
from test1.models import Post

class Commit(models.Model):
    title = models.CharField(max_length=50)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title
