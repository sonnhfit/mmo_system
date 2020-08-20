from django.db import models
from django.contrib.auth.models import AbstractUser
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


class FacebookDevice(models.Model):
    DEVICE_TYPE = [
        (0, 'default'),
        (1, 'ios'),
        (2, 'Android'),
        (3, 'Embedded computer')
    ]
    id_device = models.CharField(max_length=200, null=True, blank=True)
    device_email = models.EmailField(null=True, blank=True)
    device_type = models.IntegerField(choices=DEVICE_TYPE, default=0, blank=True, null=True)


class User(AbstractUser):
    phone_number = models.CharField(max_length=10, blank=True, null=True)
    point = models.IntegerField(default=0)


class PaymentHistory(models.Model):
    SOURCE_TYPE = [
        (0, 'default'),
        (1, 'momo'),
        (2, 'chuyen khoan'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.IntegerField(default=0)
    source = models.IntegerField(default=0, choices=SOURCE_TYPE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username


class RegisterService(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    facebook_package = models.BooleanField(default=False)
    youtube_package = models.BooleanField(default=False)
    tiktok_package = models.BooleanField(default=False)
    shoppe_package = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username


class FacebookAction(models.Model):
    action_code = models.CharField(max_length=50)
    action_name = models.CharField(max_length=255)
    action_desc = models.TextField()

    def __str__(self):
        return self.action_code


class FacebookActionScript(models.Model):
    script_code = models.CharField(max_length=50)
    script_name = models.CharField(max_length=255)
    script_desc = models.TextField()

    def __str__(self):
        return self.script_code


class FaceActScri(models.Model):
    facebook_action = models.ForeignKey(FacebookAction, on_delete=models.CASCADE)
    facebook_action_script = models.ForeignKey(FacebookActionScript, on_delete=models.CASCADE)

