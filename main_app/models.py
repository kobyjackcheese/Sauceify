from django.db import models

# Create your models here.

class Sauce(models.Model):

    name = models.CharField(max_length=100)
    img = models.CharField(max_length=250)
    description = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

# below Artist Model

class Food(models.Model):

    name = models.CharField(max_length=150)
    # img = models.CharField(max_length=500)
    sauce = models.ForeignKey(Sauce, on_delete=models.CASCADE, related_name="foods")

    def __str__(self):
        return self.name


