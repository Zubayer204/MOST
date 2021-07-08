from django.db import models
import json


class Newsletter(models.Model):
    ip = models.GenericIPAddressField(null=True, blank=True)
    email = models.EmailField()

    def __str__(self) -> str:
        return self.email + "  " + self.ip


class Visitor(models.Model):
    ip = models.GenericIPAddressField(null=True, blank=True)
    user_agent = models.TextField(null=True, blank=True)
    pages_visited = models.TextField(null=True, blank=True)
    referer = models.URLField(null=True, blank=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    visiting_time = models.DateTimeField(auto_now_add=True)
    last_visited = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.visiting_time.strftime("%Y/%m/%d  %H:%M:%S  IP-") + self.ip
    
    def set_pages(self, x):
        self.pages_visited = json.dumps(x)
    
    def get_pages(self):
        return json.loads(self.pages_visited)
