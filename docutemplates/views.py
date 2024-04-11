from django.shortcuts import render, redirect
from .models import templatedocs
from .forms import *
from docxtpl import DocxTemplate, InlineImage # type: ignore



# Create your views here.
def generatedocs(request):
    doc = DocxTemplate('inviteTmpl.docx')
    client = 'LEXLink Information Technology Services Inc.'
    address = '8-10 Woodlilly Street, Lilliesville Subdivision, Camarin Caloocan City, Philippines'
    recipient = 'Mr. John'
    context = {
        'recipientName' : recipient,
        'client' : client,
        'address'   : address,
        'evntDtStr' : 'Calcoocan City',
        'venueStr'  : '21-Oct-2021',
        'todaystr'  : '2024-03-31',
        'senderName': 'John S. Campilla',
        'bannerimg': InlineImage(doc, "images/party_banner.png")
}

    doc.render(context)
    doc.save("template4.docx")   

    return render(request, 'docutemplates/doclist.html')



def doclist(request, pk):
    docs = templatedocs.objects.filter(folder_id = pk).order_by('template_name')
    context = {
        'docs':docs
    }
    if pk == 1:
        return render(request, 'docutemplates/IPTemplates.html', context)
    else:
        return render(request, 'docutemplates/doclist.html')
   
def edittemplate(request, pk):
    docs = templatedocs.objects.get(id=pk)
    if request.method == 'POST':
        form = TemplateForms(request.POST, instance=docs)
        if form.is_valid():
            form.save()
            return redirect('templates')
        else:
            form = TemplateForms(instance=docs)
    else:
        form = TemplateForms(instance=docs)
    
    context = {
        'form' : form, 
    }
    
    return render(request, 'docutemplates/newtemplate.html', context)
    
def sampleprint(request):
    return render(request, 'docutemplates/index.html')

def processtemmplate(request):
    pass
    
def templates(request):
    templates = templatedocs.objects.all().order_by('folder', 'template_name')
    context = {
        'templates' : templates
    }
    return render(request, 'docutemplates/doclist.html', context)

def addtemplate(request):
    if request.method == 'POST':
        form = TemplateForms(request.POST)
        if form.is_valid():
            fid = request.POST['folder']
            form.save()
            return redirect('templates')
        else:
            form = TemplateForms()
    else:
        form = TemplateForms()
    
    context = {
        'form':form,
    }

    return render(request, 'docutemplates/newtemplate.html', context)



