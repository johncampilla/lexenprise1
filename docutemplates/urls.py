from django.urls import path
from . import views

urlpatterns = [
    path("templates/", views.templates, name='templates'),
    path("templates/docs/<int:pk>/'", views.doclist, name='docu-list'),
    path("templates/sampleprint/", views.sampleprint, name='docu-print'),
    path("templates/addtemplate/", views.addtemplate, name='newtemplate'),
    path("templates/edittemplate/<int:pk>/'", views.edittemplate, name='edit-template'),
    path("templates/viewtemplate/<int:pk>/", views.Viewtemplate, name='view-template'),

    path("templates/selectedmatter/<int:pk>/<int:mid>/'", views.tagselected, name='tag-matter'),

    path("templates/viewselected/<int:pk>/", views.generateselected, name='generate-selected'),
    path("templates/viewallselected/<int:pk>/", views.generateallselected, name='generate-allselected'),



    path("templates/processtemplate/", views.processtemmplate, name='process-template'),
#    path("generatedoc/processtemplate/", views.generatedocs, name='generate-docx'),

    #path("generatedoc/createdocx_fortemplate/", views.generate_reminderdoc, name='create-docx'),
    

# select matter to generate template


]