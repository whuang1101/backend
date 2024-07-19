from django.db import models

class Comments(models.Model):
    text = models.CharField(max_length = 100)   
    author = models.CharField(max_length = 100, default= "wilson") 
    date = models.DateTimeField(auto_now_add= True)
    def __str__(self) -> str:
        return self.text 