from django.db import models


class Newsletter(models.Model):
    ip = models.GenericIPAddressField(null=True, blank=True)
    email = models.EmailField()

    def __str__(self) -> str:
        return self.email + "  " + self.ip
