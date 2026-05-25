from django.db import models
from django.db.models import JSONField

class CollatzHistory(models.Model):
    """Model to store Collatz sequence history."""
    starting_number = models.IntegerField()
    sequence = JSONField()  # Store the entire sequence as JSON
    total_steps = models.IntegerField()
    max_value = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = "Collatz Histories"

    def __str__(self):
        return f"Collatz({self.starting_number}) - {self.total_steps} steps - {self.created_at.strftime('%Y-%m-%d %H:%M:%S')}"
