from django.urls import path
from . import views

urlpatterns = [
    path("templates/", views.templates, name='templates'),
    path("templates/docs/<int:pk>/'", views.doclist, name='docu-list'),
    path("templates/sampleprint/", views.sampleprint, name='docu-print'),
    path("templates/addtemplate/", views.addtemplate, name='newtemplate'),
    path("templates/edittemplate/<int:pk>/'", views.edittemplate, name='edit-template'),
    path("templates/processtemplate/", views.processtemmplate, name='process-template'),
    path("generatedoc/processtemplate/", views.generatedocs, name='generate-docx'),

# select matter to generate template


]