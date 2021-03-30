from django.db import models

class Test(models.Model) : 
    id = models.CharField(max_length=1)
    def __str__(self) -> str:
        return self.id