from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=50)
    durations = models.TextField(null=True,blank=True)
    create_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)

    def __str__(self) -> str:
        return self.title
        

