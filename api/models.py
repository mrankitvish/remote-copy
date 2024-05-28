from django.db import models
import uuid

class Notes(models.Model):
    token = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    text = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.token} {self.text}"