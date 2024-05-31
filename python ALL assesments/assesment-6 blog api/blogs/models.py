from django.db import models

class Blogs(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()  
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
