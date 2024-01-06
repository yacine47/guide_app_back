from django.db import models

# Create your models here.


class State(models.Model):
    state_name = models.CharField(default='',max_length=45)

    def __str__(self):
        return self.state_name
    
    class Meta:
        ordering = ['id']