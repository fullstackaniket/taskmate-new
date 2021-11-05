from django.db import models
from django.contrib.auth.models import User


class Tasklist(models.Model):
    task=models.CharField(max_length=300)
    done=models.BooleanField(default=False)
    manager=models.ForeignKey(User,on_delete=models.CASCADE,)

    def __str__(self):
        return self.task +" - "+ str(self.done)
