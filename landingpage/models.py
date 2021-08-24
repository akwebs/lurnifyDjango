from django.db import models


class Register(models.Model):
    name = models.CharField(max_length=255)
    dream = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=10, unique=True)
    createdAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email

class Question(models.Model):
    qid = models.CharField(max_length=20, unique=True)
    que = models.CharField(max_length=255)
    option1 = models.CharField(max_length=250, null=True)
    option2 = models.CharField(max_length=250,null=True)
    option3 = models.CharField(max_length=250,null=True)
    option4 = models.CharField(max_length=250,null=True)
