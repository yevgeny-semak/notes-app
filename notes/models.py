from django.db import models

from users.models import CustomUser


class Note(models.Model):
    title = models.CharField(max_length=50, blank=True)
    content = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    user = models.ForeignKey(CustomUser, related_name='notes_user', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        db_table='notes_note'
        verbose_name = 'Note'
        verbose_name_plural = 'Notes'
        ordering = ['-created_at', 'title']
