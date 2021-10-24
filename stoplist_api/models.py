from django.db import models

class Numbers(models.Model):
    number = models.CharField(max_length=15, null=False, blank=False)

    def __str__(self):
        return self.number
        

class Found(models.Model):
    format = models.PositiveSmallIntegerField()