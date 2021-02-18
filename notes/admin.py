from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from notes.models import Note, CustomUser
from notes.forms import CustomUserCreationForm, CustomUserChangeForm


class NoteAdmin(admin.ModelAdmin):
    model = Note
    list_display = ('id', 'title', 'created_at', 'updated_at', 'user')
    list_display_links = ('title',)
    list_filter = ('user',)
    readonly_fields = ('created_at', 'updated_at',)
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('title', 'user',)}
         ),
    )
    search_fields = ('title',)
    ordering = ('-created_at', '-updated_at')


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('id', 'email', 'username', 'is_staff', 'is_active')
    list_display_links = ('email', 'username')
    list_filter = ('email', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('email', 'username', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password1', 'password2', 'is_staff', 'is_active')}
         ),
    )
    search_fields = ('email', 'username')
    ordering = ('email', 'username')


admin.site.register(Note, NoteAdmin)
admin.site.register(CustomUser, CustomUserAdmin)
