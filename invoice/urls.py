from django.urls import path
from . import views

urlpatterns = [
    path('invoice/', views.InvoiceList, name='invoice-index'),
    path('invoice/newinvoice/', views.NewInvoice, name='new-invoice'),
    path("invoice/editinvoice/<int:pk>/'", views.EditInvoice, name='edit-invoice'),
    path("invoice/viewinvoice/<int:pk>/'", views.ViewInvoice, name='view-invoice'),
    path("invoice/invimages/<int:pk>/'", views.ViewInvoiceImage, name='view-invoice-image'),
    path('invoice/invmatters/', views.prepareinvoice, name='list-allmatters'),
    path("invoice/tempbill/<int:pk>/'", views.tobillmatter, name='invoice-matter'),
    path("invoice/viewinvoices/<int:pk>/'", views.postedinvoices, name='matter-posted-invoices'),


    path("invoice/openbillables/<int:pk>/'", views.viewbillableservices, name='billable-activities'),
    path("invoice/cancelbillables/<int:pk>/'", views.cancelbillable, name='CN_billable-activities'),


    path('invoice/newPF/', views.NewTempPf, name='invoice-newPF'),
    path("invoice/editPF/<int:pk>/'", views.EditTempPf, name='invoice-editPF'),
    path("invoice/deletePF/<int:pk>/'", views.RemoveTempPf, name='invoice-deletePF'),

    path("invoice/editPFtoOpen/<int:pk>/'", views.EditToOpen, name='invoice-toOpen'),
    path("invoice/editFeestoOpen/<int:pk>/'", views.EditFeesToOpen, name='invoice-feesOpen'),

    path("invoice/editOPEtoOpen/<int:pk>/'", views.EditOPEToOpen, name='invoice-OPEOpen'),

# urls for billing preparation
    path("invoice/billeditPF/<int:pk>/'", views.BillEditTempPf, name='invoice-editPF'),

# urls for posting to AR
    #path("posting/ToARFile/<int:pk>/'", views.BillEditTempPf, name='invoice-editPF'),

    path("testinginvoice/<int:pk>/'", views.testqry, name='test-qry'),


# ----------------------

    path('invoice/newFees/', views.NewTempFees, name='invoice-newFees'),
    path("invoice/editfees/<int:pk>/'", views.EditTempFees, name='invoice-editfees'),
    path("invoice/deleteFees/<int:pk>/'", views.RemoveTempfees, name='invoice-deletefees'),

    path("invoice/editope/<int:pk>/'", views.EditOPE, name='invoice-editOPE'),
    path("invoice/deleteOPE/<int:pk>/'", views.RemoveTempOPE, name='invoice-deleteOPE'),

]