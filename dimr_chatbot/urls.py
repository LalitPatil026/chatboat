from django.contrib import admin
from django.urls import path, include  # Import 'include'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('chatbot/', include('chatbot.urls')),  # Add this line to include chatbot app URLs
]