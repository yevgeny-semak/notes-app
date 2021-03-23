from rest_framework import serializers

from notes.models import Note
from users.models import CustomUser


class NoteSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(many=False, queryset=CustomUser.objects.all())

    class Meta:
        model = Note
        fields = '__all__'
