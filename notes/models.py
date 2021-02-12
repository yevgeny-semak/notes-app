from django.db import models


class Note(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Note'
        verbose_name_plural = 'Notes'
        ordering = ['-created_at', 'title']


class User(models.Model):
    username = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=255)
    email = models.EmailField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        ordering = ['-created_at', 'username']

