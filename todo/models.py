from django.db import models


class TODO(models.Model):
    name = models.CharField(max_length=100)
    time = models.CharField(max_length=30)
    made = models.BooleanField(default=False)
    today = models.ForeignKey('Day', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.today}'

    class Meta:
        verbose_name_plural = 'Todo'


class Day(models.Model):
    name = models.TextField()

    def __str__(self):
        return f'{self.name}'
