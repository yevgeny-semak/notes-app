from django.contrib import admin

from notes.models import Note


class NoteAdmin(admin.ModelAdmin):
    model = Note
    list_display = ('id', 'title', 'content', 'updated_at', 'user', 'is_pinned', 'is_archived')
    list_display_links = ('title', 'content',)
    list_filter = ('user',)
    readonly_fields = ('created_at', 'updated_at', 'sort_order')
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('title', 'user',)}
         ),
    )
    search_fields = ('title',)
    ordering = ('-created_at', '-updated_at')


admin.site.register(Note, NoteAdmin)
