from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    publication_date = models.DateTimeField(auto_now_add=True)
    stock_image_url = models.URLField(blank=True, null=True)  


    def __str__(self):
        return self.title
    
    