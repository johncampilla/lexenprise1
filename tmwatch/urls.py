from django.urls import path
from . import views

urlpatterns = [
    path("tmwatch/", views.gazettelist, name='publication-list'),
    path('validateopp/', views.validate_search, name='searchkeywords'),
    path("selectedOG/<int:pk>/'", views.selected_result, name='selected-OG'),
    path("viewtm/<int:pk>/'", views.viewTM, name='view-TM'),
    path('opentmresults/', views.opentmwatchresults, name='opentm-results'),

    


    
    
]