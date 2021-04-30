import datetime

from django.db import models

from users.models import CustomUser


class Note(models.Model):
    title = models.CharField(max_length=50, blank=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    sort_order = models.IntegerField(null=True, blank=True)
    is_archived = models.BooleanField(default=False)
    is_pinned = models.BooleanField(default=False)
    user = models.ForeignKey(CustomUser, related_name='notes_user', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.sort_order:
            self.sort_order = self.pk
            super().save(update_fields=['sort_order'])

    class Meta:
        db_table = 'notes_note'
        verbose_name = 'Note'
        verbose_name_plural = 'Notes'
        ordering = ['-created_at', 'title']
