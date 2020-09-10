from django.db import models

class todo_item(models.Model):
    concept=models.TextField()

    def __str__(self):
        self.concept
