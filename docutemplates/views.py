from django.shortcuts import render, redirect, HttpResponse
from .models import templatedocs
from matter.models import Matters, SelectMatters
from .forms import *
from docxtpl import DocxTemplate, InlineImage # type: ignore
import datetime
from django.conf import settings

def generate_reminderdoc(request):
    pass


def generateallselected(request, pk):
    def getdata():

        doc.render({'matter_title': selectmatter.matter_title,
                    'applicant': selectmatter.applicant,
                    'ApplicationNo': selectmatter.application_no,
                    'ApplicationDate': selectmatter.application_date,
                    'certificate_no': selectmatter.certificate_no,
                    'registration_date' : selectmatter.registration_date,
                    'publication_date' : selectmatter.publication_date,
                    'pct_appno' : selectmatter.pct_appno,
                    'pct_appdate': selectmatter.pct_appdate,
                    'lawyer': selectmatter.handling_lawyer,
                    'client_name': selectmatter.folder.client.client_name,
                    'address': selectmatter.folder.client.address,
                    'email': selectmatter.folder.client.email,
                    'template_name' : template_name})


    selected = SelectMatters.objects.all()
    docs = templatedocs.objects.get(id=pk)
    template_name = docs.template_name
    #path = 'C:\\Documents\\'+ docs.filename nfor settings.TEMPLATE_DIR
    path = settings.TEMPLATE_DIR+docs.filename
    path_docs = settings.DOCUMENTS
    
    filename = docs.filename
    doc = DocxTemplate(path)
    i =0
    for matter in selected:
        selectmatter = Matters.objects.get(id = matter.matter_id)
        client = selectmatter.folder.client.client_name
        getdata()
        i = i + 1
        doc_name = client+"-"+filename +str(i)+ ".docx"
        doc.save(path_docs+doc_name)

    return HttpResponse('')
    

# Create your views here.


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
    
    return render(request, 'docutemplates/edit_template.html', context)
    
def Viewtemplate(request, pk):
    docs = templatedocs.objects.get(id=pk)
    matters = Matters.objects.all().order_by('folder__client__client_name')
#    print(matters)
    
    context = {
        'docs' : docs,
        'matters': matters,
    }
    
    return render(request, 'docutemplates/view_template.html', context)

def generateselected(request, pk):
    docs = templatedocs.objects.get(id=pk)
    selectedmatters = SelectMatters.objects.all()
    print(selectedmatters)

    context = {
        'selectedmatters' : selectedmatters, 
        'docs' : docs,
    }
    return render(request, 'docutemplates/view_selected.html', context)

def tagselected(request, pk, mid):
    matter = Matters.objects.get(id=pk)
    selected_matter = SelectMatters()
    selected_matter.matter_id = matter.id
    selected_matter.save()
#    return  HttpResponse("selected")
    return redirect('view-template', mid)

def sampleprint(request):
    return render(request, 'docutemplates/index.html')

def processtemmplate(request):
    pass
    
def templates(request):
    SelectMatters.objects.all().delete()

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



