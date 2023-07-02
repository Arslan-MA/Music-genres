from django.db import models


class Performers(models.Model):
    name = models.CharField(max_length=80)
    data = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return f"{self.name}"

    def get_absolute_url(self):
        return f"{self.pk}"
