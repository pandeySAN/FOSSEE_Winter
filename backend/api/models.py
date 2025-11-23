from django.db import models
import json

class Dataset(models.Model):
    uploaded_at = models.DateTimeField(auto_now_add=True)
    file_name = models.CharField(max_length=255)
    summary_json = models.TextField()

    def summary(self):
        return json.loads(self.summary_json)
