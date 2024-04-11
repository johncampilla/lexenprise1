from django.shortcuts import render
from dataconversion.models import egazette, csv_matter, csv_client
from tmwatch.models import tmwatchexcemptions, TMwatchResult
from django.db.models import Q, Sum


# Create your views here.

def gazettelist(request):
    publications = egazette.objects.all()


    context = {
        'gazette' : publications,
    }

    return render(request, 'tmwatch/publicationlist.html', context)

def validate_search(request):
    def insertrecord():   
        tmresults = TMwatchResult(Application_Number = item.Application_Number,
                                 Filing_Date=item.Filing_Date,
                                 Mark = item.Mark,
                                 Applicant = item.Applicant,
                                 Nice_class = item.Nice_class,
                                 my_account_id = matter.id,
                                 myClient_Number = matter.Client_Number,
                                 myApplicationNo = matter.ApplicationNo,
                                 myPatAppNo = matter.PatAppNo,
                                 myApplicationDate = matter.ApplicationDate,
                                 myApplicant = matter.Applicant,
                                 myClientRefNo = matter.ClientRefNo,
                                 myCase1 = matter.Case1)
        tmresults.save()

    searchtable = egazette.objects.all()

#    TMmatters = csv_matter.objects.filter(ApplicationType = '4')
    TMwatchResult.objects.all().delete()
    count = 0
    for item in searchtable:
        count = count + 1
        subject = item.Mark
        searchitems = subject.split()
        for lstitem in searchitems:
            excemption = tmwatchexcemptions.objects.filter(word=lstitem)
            if excemption:
                pass
            else:
                if len(lstitem) <= 3:
                    multiple_q = Q(Q(Case1=lstitem))
                else:
                    multiple_q = Q(Q(Case1__icontains=lstitem))
                matter_list = csv_matter.objects.filter(multiple_q)
                if matter_list.exists:
                   for matter in matter_list:
                       if matter.ApplicationType == '4':
                          insertrecord()

        tmresult = TMwatchResult.objects.all().distinct('Mark')     

    context = {
        'tmresult': tmresult,
    }
                   
       
    return render(request, 'tmwatch/tmresult.html',context)

def selected_result(request, pk):
    tmresult = TMwatchResult.objects.get(id=pk)
    smark = tmresult.Mark
    qryMark = TMwatchResult.objects.filter(Mark = smark)
    context = {
        'qryMark' : qryMark,
        'tmresult':tmresult,
    }

    return render(request, 'tmwatch/TMresultDetails.html', context)

def viewTM(request, pk):
    matter = csv_matter.objects.get(id=pk)
    client = csv_client.objects.get(CLIENTNUMBER = matter.Client_Number)

    context = {
        'matter': matter,
        'client': client,
    }
    return render(request, 'tmwatch/viewmatter.html', context)

def opentmwatchresults(request):
    tmresult = TMwatchResult.objects.all().distinct('Mark')     

    context = {
        'tmresult': tmresult,
    }
       
    return render(request, 'tmwatch/tmresult.html',context)    

# def clientlist(request):
#     access_code = request.user.user_profile.userid
#     user_id = User.id

#     user_message_id = request.user.user_profile.id
#     alertmessages = inboxmessage.objects.filter(
#         messageto_id=user_message_id, status="UNREAD")
#     countalert = alertmessages.count()
#     srank = request.user.user_profile.rank
#     username = request.user.username

#     if 'q' in request.GET:
#         q = request.GET['q']
#         #clients = Client_Data.objects.filter(client_name__icontains=q)
#         multiple_q = Q(Q(client_name__icontains=q) | Q(main_contact__icontains=q) | Q(email__icontains=q) | Q(
#             address__icontains=q) | Q(industry__industry__icontains=q) | Q(status__icontains=q) | Q(country__country__icontains=q))
#         clients = Client_Data.objects.filter(
#             multiple_q).order_by("client_name")
#     else:
#         clients = Client_Data.objects.all().order_by("client_name")

#     noofclients = clients.count()
#     paginator = Paginator(clients, 11)
#     page = request.GET.get('page')
#     all_clients = paginator.get_page(page)

#     context = {
#         'page': page,
#         'noofclients': noofclients,
#         'clients': all_clients,
#         'alertmessages': alertmessages,
#         'noofalerts': countalert,
#         'username': username,
#     }

#     return render(request, 'adminapps/clientlist.html', context)

