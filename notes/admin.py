from django.contrib import admin


from notes.models import Note, User


class NoteAdmin(admin.ModelAdmin):
    model = Note
    list_display = ('id', 'title', 'created_at', 'updated_at', 'user')
    list_display_links = ('title',)
    search_fields = ('title',)


class UserAdmin(admin.ModelAdmin):
    model = User
    list_display = ('id', 'username', 'email')
    list_display_links = ('username',)
    search_fields = ('username',)


admin.site.register(Note, NoteAdmin)
admin.site.register(User, UserAdmin)
