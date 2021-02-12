from django.contrib import admin

from notes.models import Note


class NoteAdmin(admin.ModelAdmin):
    model = Note
    list_display = ('title', 'created_at', 'updated_at',)
    list_display_links = ('title',)
    search_fields = ('title',)
    ordering = ('title',)


admin.site.register(Note, NoteAdmin)
