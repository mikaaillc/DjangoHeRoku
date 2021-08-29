from django.db import models

class Todo(models.Model):
    content=models.CharField(max_length=50,verbose_name="Görev")
    completed=models.BooleanField(verbose_name="Durum")

    def __str__(self):
        return self.content