from django.db import models

# Inside your app's models.py file

# Our custom manager!
# No methods in our new manager should ever receive the whole request object as an argument! 
# (just parts, like request.POST)
class ShowsManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}

        if len(postData['title']) < 2:
            errors["title"] = "Show title should be at least 2 characters"
        if len(postData["network"]) < 5:
            errors["network"] = "Show network should be at least 5 charachters"
        if len(postData['description']) < 10:
            errors["description"] = "Show description should be at least 10 characters"
        return errors



class Shows(models.Model):
    title = models.CharField(max_length=100)
    network = models.CharField(max_length=25)
    date = models.DateField()
    description = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    objects = ShowsManager()
# Create your models here.
