from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import notesviewset

router=SimpleRouter()
router.register('notes',notesviewset,basename="notes")

urlpatterns=router.urls
