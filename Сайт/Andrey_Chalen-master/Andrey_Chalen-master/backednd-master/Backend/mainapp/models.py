from django.db import models
from django.conf import settings
from django.urls import reverse
# Create your models here.
class UserAccount(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse("account_view",
                       kwargs={"user" : self.user.name})