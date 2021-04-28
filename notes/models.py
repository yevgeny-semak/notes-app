from django.db import models

from users.models import CustomUser


class Note(models.Model):
    title = models.CharField(max_length=50, blank=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    sort_order = models.DateTimeField(auto_now_add=True)
    is_archived = models.BooleanField(default=False)
    is_pinned = models.BooleanField(default=False)
    user = models.ForeignKey(CustomUser, related_name='notes_user', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'notes_note'
        verbose_name = 'Note'
        verbose_name_plural = 'Notes'
        ordering = ['-created_at', 'title']
