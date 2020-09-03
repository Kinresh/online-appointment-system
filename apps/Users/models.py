from django.db import models

class User(models.Model):
    emailAddress= models.EmailField(max_length=100)
    name= models.CharField(max_length=50)
    phno= models.CharField(max_length=10)

    def __str__(self):
        return self.name
