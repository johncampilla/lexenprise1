from django.urls import path
from . import views



urlpatterns = [
    path('list_convertclient/', views.listclients, name = 'upload-list-clients'),
    path("selected/client_csv/<int:pk>'", views.selectedclient, name = 'selected-csv_clients'),
    path("list_converttask/<int:pk>'", views.listtask, name = 'upload-list-tasks'),
    
]
