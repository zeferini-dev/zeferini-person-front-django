from django.urls import path
from .views import PersonListView, PersonCreateView, PersonEditView, PersonDeleteView

urlpatterns = [
    path('', PersonListView.as_view(), name='person_list'),
    path('new/', PersonCreateView.as_view(), name='person_create'),
    path('<str:person_id>/edit/', PersonEditView.as_view(), name='person_edit'),
    path('<str:person_id>/delete/', PersonDeleteView.as_view(), name='person_delete'),
]
