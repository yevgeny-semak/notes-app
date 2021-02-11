from django.urls import path

from notes.views import home


urlpatterns = [
    path('notes', home, name='home'),
]