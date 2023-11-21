# candidate_app/urls.py
from django.urls import path
from .views import candidate_list, candidate_detail, candidate_create, candidate_update, candidate_delete

urlpatterns = [
    path('', candidate_list, name='candidate_list'),
    path('<int:pk>/', candidate_detail, name='candidate_detail'),
    path('new/', candidate_create, name='candidate_create'),
    path('<int:pk>/edit/', candidate_update, name='candidate_update'),
    path('<int:pk>/delete/', candidate_delete, name='candidate_delete'),
]
