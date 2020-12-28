from rest_framework import serializers
from .models import notes

class Noteserializer(serializers.ModelSerializer):
    class Meta:
        fields=("id", "title", "content", "created", "updated")
        model=notes
