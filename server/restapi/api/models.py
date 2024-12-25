from django.db import models

# Create your models here.
class Answer(models.Model):
    text = models.CharField(max_length=1024)

    def __str__(self):
        return self.text