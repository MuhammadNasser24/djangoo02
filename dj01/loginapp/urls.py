from django.urls import path
from .views import about

# Create your urls here

urlpatterns = [
    path('login/', about),
]