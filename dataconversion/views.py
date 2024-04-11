from django.http import HttpResponse
from django.shortcuts import render
from .models import Csv, csv_client, csv_matter, csv_task, csv_duedates,csv_AR


import csv


# Create your views here.
# def upload_file_view(request):

#     form = CsvForm(request.POST or None, request.FILES or None)

#     if form.is_valid():
#         form.save()
#         form = CsvForm()
#         obj = Csv.objects.get(activated = False)
#         print(obj)
#         with open(obj.file_name.path, 'r') as f:
#             reader = csv.reader(f)

#             for i, row in enumerate(reader):
#                 if i==0:
#                     pass
#                 else:
#                     row = "".join(row)
#                     row = row.replace(";", " ")
#                     row = row.split()
#                     print(row)
#                     print(type(row))
#             obj.activated = True
#             obj.save()

        

#     context = {
#         'form' : form,
#     }
    
    
#     return render(request, 'dataconversion/upload.html',context)

def listclients(request):
    #csv_client.objects.all().delete()
    clients = csv_client.objects.all()
    

    context = {
        'clients': clients
    }

    return render(request, 'dataconversion/listclients.html',context)

def listmatters(request):
    matters = csv_matter.objects.all()

    context = {
        'matters': matters
    }

    return render(request, 'dataconversion/listmatters.html',context)

def listtask(request, pk):
    matter = csv_matter.objects.get(id=pk)
    tasks = csv_task.objects.filter(ApplicationNo = matter.ApplicationNo, ClientNo = matter.Client_Number)
    duedates = csv_duedates.objects.filter(ApplicationNo = matter.ApplicationNo, ClientNo = matter.Client_Number)
    context = {
        'matter': matter,
        'tasks': tasks,
        'duedates': duedates,
    }

    return render(request, 'dataconversion/listtasks.html',context)

def selectedclient(request, pk):
    client = csv_client.objects.get(id=pk)
    matter = csv_matter.objects.filter(Client_Number = client.CLIENTNUMBER)
    invoices = csv_AR.objects.filter(Client_Number = client.CLIENTNUMBER) 
    
    context = {
        'matters' : matter,
        'client' : client,
        'invoices': invoices,
    }
    return render(request, 'dataconversion/listmatters.html', context)

