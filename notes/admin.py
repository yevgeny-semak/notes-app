from django.contrib import admin

from notes.models import Note, User


class NoteAdmin(admin.ModelAdmin):
    model = Note
    list_display = ('id', 'title', 'created_at', 'updated_at',)
    list_display_links = ('title',)
    search_fields = ('title',)
    ordering = ('title',)


class UserAdmin(admin.ModelAdmin):
    model = User
    list_display = ('id', 'username', 'email')
    list_display_links = ('username',)
    search_fields = ('username',)
    ordering = ('username', 'created_at',)


admin.site.register(Note, NoteAdmin)
admin.site.register(User, UserAdmin)