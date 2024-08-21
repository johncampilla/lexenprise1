from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import task_detail, FilingDocs
from matter.models import Matters
from reference_lookup.models import CaseType
from docutemplates.models import templatedocs
from taskcode_settings.models import ActivityCodes, FilingFeeCodes, TaskTemplates
from client.models import Client_Data
from invoice.models import TempBills, TempFilingFees, TempOPE
from casefolder.models import Lawyer_Data, CaseFolder
from .forms import ActivityForm, OutgoingActivityForm, IncomingActivityForm, filingdocforms 
from invoice.forms import TempBillsForm, TempFeesForm, TempExpFeesForm
from django.urls import reverse, reverse_lazy
from django.contrib import messages
import string
from django.contrib.auth.decorators import login_required  # type: ignore
from django.conf import settings
from docxtpl import DocxTemplate, InlineImage # type: ignore



@login_required
def DocketingListView(request):
    activities = task_detail.objects.all().order_by('-tran_date')

    context={
        'activities' : activities 
    }

    return render(request, 'activity/index.html', context)

@login_required
def NewActivity(request, mid):
    matter = Matters.objects.get(id=mid)
    if request.method == 'POST':
        form = ActivityForm(request.POST)
        if form.is_valid():
            activity_rec = form.save(commit=False)
            activity_rec.matter_id = matter.id
            activity_rec.save()            
            form.save()
            return redirect('select-matter', mid)
        else:
            print('invalid ang form pre 1')
            form = ActivityForm()
    else:
        print('invalid ang form pre 2')
        form = ActivityForm()

    context = {
        'form': form,
        'matter':matter,
    }
    return render(request, 'activity/newactivity.html', context)   

@login_required
def EditActivity(request, pk):
    activity = task_detail.objects.get(id=pk)
    mid = activity.matter_id
    matter = Matters.objects.get(id=mid)
    if request.method == 'POST':
        form = ActivityForm(request.POST, instance=activity)
        if form.is_valid():
            form.save()
            return redirect('select-activity', activity.id)
        else:
            form = ActivityForm(instance=activity)
    else:
        form = ActivityForm(instance=activity)

    context = {
        'form': form,
        'matter':matter,
        'activity': activity,
    }
    return render(request, 'activity/editactivity.html', context)

@login_required
def ActivityWithTemplate(request, pk, mid):
    activity = task_detail.objects.get(id=pk)
    tid = activity.id
    print(tid)
    templates = TaskTemplates.objects.filter(task_id = activity.task_code_id)
    sid = mid
    matter = Matters.objects.get(id=mid)

    form = ActivityForm(instance=activity)

    context = {
        'sid': sid,
        'matter': matter,
        'activity': activity,
        'templates': templates,
        'tid' : tid
    }
    return render(request, 'activity/activitywtemplates.html', context)


def generatedocs(request, pk, mid, tid):
    doc = TaskTemplates.objects.get(id=pk)
    template = templatedocs.objects.get(id = doc.template_id)
    filename = template.filename  
    matter = Matters.objects.get(id=mid)
    matter_title = matter.matter_title
    applicant = matter.applicant
    application_no = matter.application_no
    application_date = matter.application_date
    certificate_no = matter.certificate_no
    registration_date = matter.registration_date
    nice_class = matter.nice_class
    casefolder = CaseFolder.objects.get(id = matter.folder_id)
    client = Client_Data.objects.get(id = casefolder.client_id)
    client_name = client.client_name
    client_address = client.address
    recipient = client.account_person
    email = client.email
    doc = DocxTemplate("templates/"+filename)
    print(doc)
    context = {
        'matter_title': matter_title,
        'applicant': applicant,
        'application_no' : application_no,
        'application_date' : application_date,
        'certificate_no' : certificate_no,
        'registration_date':registration_date,
        'nice_class' : nice_class,
        #client info
        'client_name' : client_name,
        'client_address': client_address,
        'contact': recipient,
        'email': email,
        'pk' : pk,
    }
#    print(context)
    doc.render(context)
    print('pati d2', doc)
    
    print(settings.TEMPLATEDOCS)
    doc.save("C:\\Documents\\"+filename)  
    #tempdir = settings.TEMPLATEDOCS 
    #doc.save(tempdir+'+filename)   
    

    return redirect('view-activitywtemplates', tid, mid)


#    return render(request, 'docutemplates/doclist.html')    

@login_required
def ViewActivity(request, pk, mid):
    activity = task_detail.objects.get(id=pk)
    sid = mid
    matter = Matters.objects.get(id=mid)
    docs = FilingDocs.objects.filter(task_detail_id = pk)
    form = ActivityForm(instance=activity)

    context = {
        'form': form,
        'sid': sid,
        'matter': matter,
        'activity': activity,
        'docs' : docs,
    }
    return render(request, 'activity/view_activity.html', context)

def AttachDocument(request, pk):
    task = task_detail.objects.get(id=pk)
    matter = Matters.objects.get(id = task.matter_id)
    user_name = request.user.username

    if request.method == 'POST':
        form = filingdocforms(request.POST, request.FILES)
        if form.is_valid():
            document_rec = form.save(commit=False)
            document_rec.task_detail_id = task.id
            document_rec.createdby = user_name
            document_rec.save()            
            return redirect('view-activity', task.id, task.matter_id)
        else:
            form = filingdocforms()
    else:
        form = filingdocforms()

    context = {
        'form': form,
        'matter':matter,
        'task' : task,
    }
    return render(request, 'matter/newactivitydocs.html', context) 


@login_required
def viewattachdocument(request, pk):
    docs = FilingDocs.objects.get(id=pk) 
    task = task_detail.objects.get(id = docs.task_detail_id) 
    print(task)
    matter = Matters.objects.get(id = docs.task_detail.matter_id)
    user_name = request.user.username
    print(matter)
    form = filingdocforms(instance=docs)
    if request.method == "POST":
        form = filingdocforms(request.POST, request.FILES, instance=docs)
        if form.is_valid():
            document_rec = form.save(commit=False)
            document_rec.task_detail_id = task.id
            document_rec.updatedby = user_name
            document_rec.save()            
            return redirect('view-activity', task.id, matter.id)
        else:
            form = filingdocforms(instance=docs)
    else:
        form = filingdocforms(instance=docs)

    context = {
        'docs':docs,
        'matter':matter,
        'form' : form,
        'task' : task
    }
    # return render(request, 'matter/viewactivitydocs.html', context)
    return render(request, 'activity/newactivitydocs.html', context)   

@login_required
def selectdocument(request, pk):
    docs = FilingDocs.objects.get(id=pk) 
    task = task_detail.objects.get(id = docs.task_detail_id) 
    print(task)
    matter = Matters.objects.get(id = docs.task_detail.matter_id)
    user_name = request.user.username
    print(matter)
    form = filingdocforms(instance=docs)
    if request.method == "POST":
        form = filingdocforms(request.POST, request.FILES, instance=docs)
        if form.is_valid():
            document_rec = form.save(commit=False)
            document_rec.task_detail_id = task.id
            document_rec.updatedby = user_name
            document_rec.save()            
            return redirect('view-activity', task.id, matter.id)
        else:
            form = filingdocforms(instance=docs)
    else:
        form = filingdocforms(instance=docs)

    context = {
        'docs':docs,
        'matter':matter,
        'form' : form,
        'task' : task
    }
    # return render(request, 'matter/viewactivitydocs.html', context)
    return render(request, 'activity/selectdocs.html', context)   


@login_required
def RemoveActivity(request, pk):
    activity = task_detail.objects.get(id=pk)
    if request.method == 'POST':
        activity.delete()
        return redirect('task-list') 
    
    object = {
        'activity' : activity
    }
    
    return render(request, 'activity/delete.html', object)
    
    return redirect('task-list')

@login_required
def matterlist(request):
    matters = Matters.objects.all().order_by('-filing_date')
    docketlist = task_detail.objects.all().order_by('-tran_date')
    documents = FilingDocs.objects.all().order_by('-datecreated', 'DocDate')
    outform = OutgoingActivityForm
    inform = IncomingActivityForm

    context = {
        'matters': matters,
        'docketlist': docketlist,
        'outform': outform,
        'inform': inform,
        'documents': documents,
    }

    return render(request, 'activity/docketlist.html', context)

@login_required
def NewOutgoingActivity(request):
    def createbilableserviceIP():
        bill_description = billcode_rec.bill_description
        bill_amountUSD = billcode_rec.amount
        bill_amountPHP = billcode_rec.pesoamount
        preparedby = lawyer_rec.access_code
        billing = TempBills(
            matter_id = mid, 
            tran_date = request.POST['tran_date'], 
            task_id = sTask_ID,
#            spentinhrs = request.POST['spentinhrs'],
#            spentinmin = request.POST['spentinmin'],
            service_rendered = bill_description,
            USDamount = bill_amountUSD,
            PhPamount = bill_amountPHP,
            recordedby = preparedby,
            status = 'Open',
            )
        billing.save()
        for filing in filingfees:
            fees = TempFilingFees(
                tran_date = request.POST['tran_date'], 
                filing_particulars = filing.fee_description,
                USDamount = filing.amount,
                PhPamount = filing.pesoamount,
                matter_id = mid,
#                service_id = sTask_ID,
                status = "Open",
            )
            fees.save()

    if request.method == 'POST':
        form = OutgoingActivityForm(request.POST)
        if form.is_valid():
            outgoingrec = form.save(commit=False)
            task_code = request.POST['task_code']
            tran_type = request.POST['tran_type']
            tran_date = request.POST['tran_date']
            lawyer_id = request.POST['lawyer']

            mid = request.POST['matter']
            matter = Matters.objects.get(id = mid)

            case_type_id = matter.case_type_id
            case_type = CaseType.objects.get(id = case_type_id)
            if task_code:
                billcode_rec = ActivityCodes.objects.get(id = task_code)
            
            lawyer_rec = Lawyer_Data.objects.get(id = lawyer_id)
            if task_code:
                filingfees = FilingFeeCodes.objects.filter(ActivityCode_id = task_code)
            outgoingrec.save()
            sTask_ID = outgoingrec.id

            if tran_type == 'Billable' :
                if case_type.case_type == 'IP Filings':
                    createbilableserviceIP()
            
            return redirect('task-list')

@login_required    
def NewIncomingActivity(request):
    if request.method == 'POST':
        form = IncomingActivityForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task-list')
        
@login_required
def SelectedActivity(request, pk):
    task = task_detail.objects.get(id = pk)
    mid = task.matter_id
    activities = task_detail.objects.filter(matter_id = mid).order_by('-tran_date')
    trandate = task.tran_date
    billables = TempBills.objects.filter(tran_date = trandate, matter_id = mid)
    tempfees = TempFilingFees.objects.filter(tran_date = trandate, matter_id = mid)
    tempOPE = TempOPE.objects.filter(matter_id = mid)
    matter = Matters.objects.get(id = mid)

    context = {
        'matter' : matter,
        'task' : task,
        'tempbills' : billables,
        'tempfees' : tempfees,
        'activities' : activities,
        'tempOPE' : tempOPE,
    }
    return render(request, 'activity/selected_activitydetail.html', context)

@login_required
def edittempbills(request, pk):
    tempbills = TempBills.objects.get(id=pk)
    task_id = tempbills.task_id
    task = task_detail.objects.get(id=task_id)
    mid = tempbills.matter_id
    matter = Matters.objects.get(id=mid)

    if request.method == 'POST':
        form = TempBillsForm(request.POST, instance=tempbills)
        if form.is_valid():
            form.save()
            return redirect('select-activity', task_id)
        else:
            form = TempBillsForm(instance=tempbills)
    else:
        form = TempBillsForm(instance=tempbills)
    
    context = {
        'form' : form,
        'matter': matter,
        'tempbills': tempbills,
        'task': task,
    }
    return render(request, 'activity/edittempbills.html', context)

def RemoveExpense(request, pk, TID):
    tempope = TempOPE.objects.get(id = pk)
    task = task_detail.objects.get(id = TID)
    tempope.delete()
    return redirect('select-activity', TID)


def AddExpense(request, pk):
    task = task_detail.objects.get(id = pk)
    mid = task.matter_id    
    matter = Matters.objects.get(id=mid)
    peso_rate = settings.EXCHANGE_RATE
    if request.method == 'POST':
        form = TempExpFeesForm(request.POST)
        if form.is_valid():
            expense_rec = form.save(commit=False)
            expense_rec.matter_id = matter.id
            if expense_rec.USDamount > 0:
                if expense_rec.PhPamount > 0:
                    x=1
                else:
                    expense_rec.PhPamount = expense_rec.USDamount * peso_rate
            else:
                if expense_rec.PhPamount > 0 :
                    expense_rec.USDamount = expense_rec.PhPamount / 44.00

            expense_rec.save()            
            form.save()
            return redirect('select-activity', pk)
        else:
            form = TempExpFeesForm()
    else:
        form = TempExpFeesForm()

    context = {
        'form': form,
        'matter':matter,
    }
    return render(request, 'activity/newope.html', context)   

@login_required
def edittempfees(request, pk):
    tempfees = TempFilingFees.objects.get(id=pk)
    matter  = Matters.objects.get(id = tempfees.matter_id)

    if request.method == 'POST':
        form = TempFeesForm(request.POST, instance=tempfees)
        if form.is_valid():
            form.save()
            return redirect('task-list')
        else:
            form = TempFeesForm(instance=tempfees)
    else:
        form = TempFeesForm(instance=tempfees)
    
    context = {
        'form' : form,
        'matter': matter,
        'tempfees': tempfees,
    }
    return render(request, 'activity/edittempfees.html', context)

@login_required
def removetembills(request, pk):
    tempbills = TempBills.objects.get(id=pk)
    task_id = tempbills.task_id
    tempbills.delete()
    return redirect('select-activity', task_id)

def RemoveAttachDocument(request, pk, mid):
    docfile = FilingDocs.objects.get(id = pk)
    task_id = docfile.task_detail_id
    docfile.delete()
    return redirect('view-activity', task_id, mid )
