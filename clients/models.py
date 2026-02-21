from django.db import models

# Information of the Client
class Client(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return self.first_name, self.last_name