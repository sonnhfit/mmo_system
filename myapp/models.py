from django.db import models

# Create your models here.


class FacebookUser(models.Model):
    email = models.EmailField(null=True)
    phone = models.CharField(max_length=10, null=True)
    password = models.CharField(null=True, max_length=40)
    cookie = models.TextField(null=True, blank=True)
    fa2 = models.CharField(max_length=255)
    number_of_friend = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.email
