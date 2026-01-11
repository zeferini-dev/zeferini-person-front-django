"""URL configuration for TesteFull Django frontend."""
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(url='/persons/', permanent=False), name='home'),
    path('persons/', include('persons.urls')),
]
