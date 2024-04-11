from django.urls import path
from . import views

urlpatterns = [
    # path('activity/', views.DocketingListView, name='task-list'),
    path('activity/', views.matterlist, name='task-list'),
    path("activity/add/<int:mid>/'", views.NewActivity, name='new-activity'),
    path("activity/del/<int:pk>/'", views.RemoveActivity, name='delete-activity'),
    path("activity/edit/<int:pk>/'", views.EditActivity, name='edit-activity'),
    #4/1/2024
    path("viewactivitywithtemplates/<int:pk>/<int:mid>/'", views.ActivityWithTemplate, name='view-activitywtemplates'),    
    path("generatedoc/processtemplate/<int:pk>/<int:mid>/<int:tid>'", views.generatedocs, name='generate-docx'),
    #2/21/2023
    path("activity/viewactivity/<int:pk>/<int:mid>/'", views.ViewActivity, name='view-activity'),
    path("activity/viewattachdocs/<int:pk>/'", views.viewattachdocument,  name='view-attach'),
    path("activity/selectdocs/<int:pk>/'", views.selectdocument,  name='select-doc'),
    path("activity/attachdocs/<int:pk>/'", views.AttachDocument, name='attachdocument'),
    path("activity/removeattach/<int:pk>/<int:mid>/'", views.RemoveAttachDocument, name='remove-attachdocument'),



    path("activity/newoutgoing/", views.NewOutgoingActivity, name='outgoing'),
    path("activity/newincoming/", views.NewIncomingActivity, name='incoming'),
    path("activity/selectactivity/<int:pk>/'", views.SelectedActivity, name='select-activity'),
    path("activity/edittempbill/<int:pk>/'", views.edittempbills, name='edit-tempbills'),
    path("activity/removetempbill/<int:pk>/'", views.removetembills, name='remove-tempbills'),

    path("activity/edittempfees/<int:pk>/'", views.edittempfees, name='edit-tempfees'),

    path("activity/addexpense/<int:pk>/'", views.AddExpense, name='new-expense'),
    path("activity/removeexpense/<int:pk>/<int:TID>/'", views.RemoveExpense, name='new-removeexpense'),


]