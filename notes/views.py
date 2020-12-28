from django.shortcuts import render
from rest_framework import viewsets
from .models import notes
from .serializers import Noteserializer
from rest_framework import permissions
from rest_framework.exceptions import PermissionDenied

# Create your views here.


class is_owner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user


class notesviewset(viewsets.ModelViewSet):
    serializer_class = Noteserializer
    permission_classes = (is_owner,)

    def get_queryset(self):
        user = self.request.user

        if user.is_authenticated:
            return notes.objects.filter(owner=user)
        raise PermissionDenied()

    # this function is used to ensure the owner is the user
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
