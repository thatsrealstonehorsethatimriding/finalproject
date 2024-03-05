from django.db import models

class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.EmailField()
    lastLogin = models.DateTimeField(auto_now=True)

    class Meta:
        app_label ='finalapp1'

