from django.shortcuts import render, redirect
from .models import *
from activity.models import task_detail
from client.models import Client_Data
from matter.models import Matter_Applicant, AppType, CaseType
from .forms import *
from django.db import connection
from django.db.models import Q, Sum

# Create your views here.
def InvoiceList(request):
    invoice = AccountsReceivable.objects.all().order_by("-bill_date")
    context = {
        'invoices' : invoice,
    }
    return render(request, 'invoice/invoice_list.html', context)

def ViewInvoiceImage(request, pk):

    try:
        invimg = InvoiceImage.objects.get(id = pk)
    except InvoiceImage.DoesNotExist:
        invimg = None
    print(invimg)
    context = {
        'invimg' : invimg, 
    }

    return render(request, 'invoice/invoice_image.html', context)




def ViewInvoice(request, pk):
    invoice = AccountsReceivable.objects.get(id=pk)
    mid = invoice.matter_id
    matter = Matters.objects.get(id = mid)
    activities = task_detail.objects.filter(matter_id = mid)
    applicants = Matter_Applicant.objects.filter(matter__id = mid)
    bills = Bills.objects.filter(ar__id = pk)
    filing_fees = FilingFees.objects.filter(ar__id = pk)
    ope = OPE.objects.filter(ar__id = pk)
    sid = pk
    cid = invoice.matter.folder.client_id
    client = Client_Data.objects.get(id = cid)

    try:
        invimg = InvoiceImage.objects.filter(ar__id = pk)
    except InvoiceImage.DoesNotExist:
        invimg = None



    stype = CaseType.objects.get(id=sid)
    apptype_id = matter.apptype.id
    sapptype = AppType.objects.get(id=apptype_id)

    context = {
        'bills': bills,
        'filing_fees': filing_fees,
        'OPE' : ope,
        'invoice' : invoice,
        'matter': matter,
        'client': client,
        'applicants' : applicants,
        'activities' : activities,
        'invimg' :  invimg
    }

    if sapptype != 'NONIP':
        return render(request, 'invoice/invoice_detail_IP.html', context)
    else :
        return render(request, 'invoice/invoice_detail', context)

def EditInvoice(request, pk):
    pf = AccountsReceivable.objects.get(id=pk)
    bills = Bills.objects.filter(ar__id = pk)
    filing_fees = FilingFees.objects.filter(ar__id = pk)
    sid = pk
    if request.method == 'POST':
        form = InvoiceForm(request.POST, instance=pf)
        if form.is_valid():
            form.save()
            return redirect('invoice-index')
        else:
            form = InvoiceForm(instance=pf)
    else:
        form = InvoiceForm(instance=pf)

    context = {
        'form': form,
        'bills': bills,
        'filings': filing_fees,
    }
    return render(request, 'invoice/editinvoice.html', context)

def NewInvoice(request):
    if request.method == 'POST':
        form = InvoiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('invoice-index')
        else:
            form = InvoiceForm()
    else:
        form = InvoiceForm()

    context = {
        'form': form,
    }
    return render(request, 'invoice/editinvoice.html', context)

def prepareinvoice(request):
    matters = Matters.objects.all().order_by('-filing_date')

    context = {
        'matters':matters,
    }

    return render(request, 'invoice/allmatters.html', context)

def postedinvoices(request, pk):
    matter = Matters.objects.get(id = pk)
    invoices = AccountsReceivable.objects.filter(matter_id = pk)
    context = {
        'invoices' : invoices,
        'matter' : matter
    }
    return render(request, 'invoice/matter_postedinvoices.html', context)

def tobillmatter(request, pk):
    matter = Matters.objects.get(id = pk)

    temppf = TempBills.objects.filter(matter_id = pk, status="Open")
    total_amount = TempBills.objects.filter(matter_id=pk, status="Open").aggregate(Sum('USDamount'))
    bill_amt_USD = total_amount["USDamount__sum"]    
    total_amount = TempBills.objects.filter(matter_id=pk, status="Open").aggregate(Sum('PhPamount'))
    bill_amt_PHD = total_amount["PhPamount__sum"] 

    tempfees = TempFilingFees.objects.filter(matter_id =pk, status="Open")
    total_amount = TempFilingFees.objects.filter(matter_id=pk, status="Open").aggregate(Sum('USDamount'))
    fees_amt_USD = total_amount["USDamount__sum"]    
    total_amount = TempFilingFees.objects.filter(matter_id=pk, status="Open").aggregate(Sum('PhPamount'))
    fees_amt_PHD = total_amount["PhPamount__sum"] 

    tempOPE = TempOPE.objects.filter(matter_id = pk, status="Open")
    total_amount = TempOPE.objects.filter(matter_id=pk, status="Open").aggregate(Sum('USDamount'))
    ope_amt_USD = total_amount["USDamount__sum"]    
    total_amount = TempOPE.objects.filter(matter_id=pk, status="Open").aggregate(Sum('PhPamount'))
    ope_amt_PHD = total_amount["PhPamount__sum"] 
   
    context = {
        'tempbills' : temppf,
        'tempfees' : tempfees,
        'tempOPE' : tempOPE,
        'matter' : matter,
        'pf_USD' : bill_amt_USD,
        'pf_PhP' : bill_amt_PHD,
        'fees_USD' : fees_amt_USD,
        'fees_PhP' : fees_amt_PHD,
        'Ope_USD' : ope_amt_USD,
        'Ope_PhP' : ope_amt_PHD

#        'formPF' : formPF,
#        'formFees':formFees,
    }
    return render(request, 'invoice/matter_invoicedetail.html', context)

def viewbillableservices(request,pk):
    matter = Matters.objects.get(id = pk)

    temppf = TempBills.objects.filter(matter_id = pk).order_by('-tran_date')
    tempfees = TempFilingFees.objects.filter(matter_id = pk)
    tempOPE = TempOPE.objects.filter(matter_id = pk)

    context = {
        'tempbills': temppf,
        'tempfees': tempfees,
        'tempOPE': tempOPE,
        'matter' : matter,
    }
    return render(request, 'invoice/matter_billableactivities.html', context)

def EditToOpen(request, pk):
    temppf = TempBills.objects.get(id = pk)
    matter = Matters.objects.get(id = temppf.matter_id)
    print(matter)
    if temppf.status == 'Proforma' or 'Cancelled' :
        temppf.status = 'Open'
        temppf.save()
    elif temppf.status == 'Open' :
        temppf.status = 'Proforma'
        temppf.save()

    return redirect('billable-activities', matter.id) 

def EditOPEToOpen(request, pk):
    tempope = TempOPE.objects.get(id = pk)
    matter = Matters.objects.get(id = tempope.matter_id)
    if tempope.status == 'Proforma' or 'Cancelled' :
        tempope.status = 'Open'
        tempope.save()
    elif tempope.status == 'Open' :
        tempope.status = 'Proforma'
        tempope.save()

    return redirect('billable-activities', matter.id)    


def EditFeesToOpen(request, pk):
    tempfees = TempFilingFees.objects.get(id = pk)
    matter = Matters.objects.get(id = tempfees.matter_id)
    print(matter)
    if tempfees.status == 'Proforma' or 'Cancelled' :
        tempfees.status = 'Open'
        tempfees.save()
    elif tempfees.status == 'Open' :
        tempfees.status = 'Proforma'
        tempfees.save()

    return redirect('billable-activities', matter.id)    

def cancelbillable(request, pk):
    temppf = TempBills.objects.get(id = pk)
    matter = Matters.objects.get(id = temppf.matter_id)
    temppf.status = 'Cancelled'
    temppf.save()
    return redirect('billable-activities', matter.id) 



def NewTempPf(request):
    if request.method == 'POST':
        form = TempBillsForm(request.POST)
        if form.is_valid():
            tempbill_rec = form.save(commit=False)
            tempbill_rec.matter_id = request.POST['matter']
            tempbill_rec.save()
            return redirect('invoice-matter', request.POST['matter'])

def NewTempFees(request):
    if request.method == 'POST':
        form = TempFeesForm(request.POST)
        if form.is_valid():
            tempfees_rec = form.save(commit=False)
            tempfees_rec.matter_id = request.POST['matter']
            tempfees_rec.save()
            return redirect('invoice-matter', request.POST['matter'])

def EditTempPf(request, pk):
    pf = TempBills.objects.get(id=pk)
    matter = Matters.objects.get(id = pf.matter_id)
    if request.method == 'POST':
        form = TempBillsForm(request.POST, instance=pf)
        if form.is_valid():
            form.save()
            return redirect('billable-activities', matter.id)        
        else:
            form = TempBillsForm(instance=pf)
    else:
        form = TempBillsForm(instance=pf)

    context = {
        'form': form,
        'pf': pf,
        'matter': matter,
    }
    return render(request, 'invoice/invoice_edittemppf.html', context)

def BillEditTempPf(request, pk):
    pf = TempBills.objects.get(id=pk)
    matter = Matters.objects.get(id = pf.matter_id)
    if request.method == 'POST':
        form = TempBillsForm(request.POST, instance=pf)
        if form.is_valid():
            form.save()
            return redirect('invoice-matter', matter.id)    
        else:
            form = TempBillsForm(instance=pf)
    else:
        form = TempBillsForm(instance=pf)

    context = {
        'form': form,
        'pf': pf,
        'matter': matter,
    }
    return render(request, 'invoice/invoice_edittemppf.html', context)

def testqry_(request):
    data = TempBills.objects.all()
    print(data)
    print(data.query)
    print(connection.queries)

    context = {
        'data' : data,
    }
    
    return render(request, 'invoice/test.html', context)

def testqry_1(request, pk):
    PF = TempBills.objects.filter(Q(matter_id=pk) & Q(status = 'Open'))

    total_amount = TempBills.objects.filter(matter_id=pk).aggregate(Sum('USDamount'))
    bill_amt = total_amount["USDamount__sum"]    
    print(bill_amt)
    FILING = TempFilingFees.objects.filter(Q(matter_id=pk) & Q(status = 'Open'))
    OPE = TempOPE.objects.filter(Q(matter_id=pk) & Q(status = 'Open'))

    print(PF)
    # print(data.query)
    # print(connection.queries)


    context = {
        'PF' : PF,
    #    'billTotal':billTotal,
        'FILING':FILING,
        'OPE' : OPE,
        'bill_amt': bill_amt,
    }
    
    return render(request, 'invoice/test.html', context)

def testqry(request, pk):


    return render(request, 'invoice/test.html', context)

def RemoveTempPf(request, pk):
    temppf = TempBills.objects.get(id=pk)
    mid = temppf.matter_id
    temppf.delete()
    return redirect('invoice-matter', mid)

def EditOPE(request,pk):
    ope = TempOPE.objects.get(id=pk)
    matter = Matters.objects.get(id = ope.matter_id)
    if request.method == 'POST':
        form = TempExpFeesForm(request.POST, instance=ope)
        if form.is_valid():
            form.save()
            return redirect('billable-activities', matter.id)
        else:
            form = TempExpFeesForm(instance=ope)
    else:
        form = TempExpFeesForm(instance=ope)

    context = {
        'form': form,
        'ope': ope,
        'matter': matter,
    }
    return render(request, 'invoice/invoice_editope.html', context)

def EditTempFees(request, pk):
    fees = TempFilingFees.objects.get(id=pk)
    matter = Matters.objects.get(id = fees.matter_id)
    if request.method == 'POST':
        form = TempFeesForm(request.POST, instance=fees)
        if form.is_valid():
            form.save()
            return redirect('billable-activities', matter.id)
        else:
            form = TempFeesForm(instance=fees)
    else:
        form = TempFeesForm(instance=fees)

    context = {
        'form': form,
        'fees': fees,
        'matter': matter,
    }
    return render(request, 'invoice/invoice_edittempfees.html', context)

def RemoveTempfees(request, pk):
    tempfees = TempFilingFees.objects.get(id=pk)
    mid = tempfees.matter_id
    tempfees.delete()
    return redirect('invoice-matter', mid)

def RemoveTempOPE(request, pk):
    tempope = TempOPE.objects.get(id = pk)
    matter = Matters.objects.get(id = tempope.matter_id)
    print(matter)
    if tempope.status == 'Proforma' :
        tempope.status = 'Open'
        tempope.save()
    elif tempope.status == 'Open' :
        tempope.status = 'Proforma'
        tempope.save()

    return redirect('billable-activities', matter.id)