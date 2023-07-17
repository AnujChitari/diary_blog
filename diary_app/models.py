from django.db import models
from django.utils import timezone

from datetime import datetime

# Create your models here.

class DiaryEntry(models.Model):
    title = models.CharField(max_length=255, default='Default Title')
    entry_date = models.DateTimeField(default=timezone.now)
    # entry_date = models.DateTimeField(null=True)
    content = models.TextField()

    class Meta:
        app_label = 'diary_app'
        
    def __str__(self):
        return str(self.entry_date)
