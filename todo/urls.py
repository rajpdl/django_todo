from django.urls import path, include
from .views import all, delete, create

urlpatterns = [
    path('all', all, name="all"),
    path('delete/<int:id>', delete, name="delete"),
    path('create', create, name="create"),
]