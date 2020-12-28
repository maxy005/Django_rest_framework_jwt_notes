from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# -------my second user in admin -------
# second_user=manthan
# password=djangorestframework

class notes(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    title = models.CharField(max_length=200,null=True)
    content = models.TextField(null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
