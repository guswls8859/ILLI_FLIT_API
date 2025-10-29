from django.db import models

# Create your models here.
class User_model(models.Model):
    user_id = models.CharField(max_length=30, null=False)
    password = models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.user_id


class User_profile(models.Model):
    User_model = models.OneToOneField(User_model, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    agency = models.CharField(max_length=100, null=True)
    user_type = models.IntegerField(default=0)


    def __str__(self):
        return self.name

class Payment_user(models.Model):
    test = models.CharField(max_length=10, null=False)

    def __str__(self):
        return self.test