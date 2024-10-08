from django.db import models

# Create your models here.

class Csv(models.Model):
    file_name = models.FileField(upload_to='csvs', blank=True, null=True)
    uploaded = models.DateTimeField(auto_now_add=True)
    activated = models.BooleanField(default=False)

    def __str__(self):
        return f"File ID : {self.id} - {self.file_name}"



class csv_client(models.Model):

    CLIENTNUMBER = models.CharField(max_length=25, blank=True, null=True)
    EntityType = models.CharField(max_length=15, blank=True, null=True)
    ClientName = models.CharField(max_length=200, blank=True, null=True)
    UnitDescription = models.CharField(max_length=100, blank=True, null=True)
    Street = models.CharField(max_length=100, blank=True, null=True)
    City = models.CharField(max_length=100, blank=True, null=True)
    State_Prov = models.CharField(max_length=100, blank=True, null=True)
    Country = models.CharField(max_length=60, blank=True, null=True)
    Fax_Number = models.CharField(max_length=60, blank=True, null=True)
    EMail = models.CharField(max_length=100, blank=True, null=True)
    URL = models.CharField(max_length=60, blank=True, null=True)
    Zip_Code = models.CharField(max_length=25, blank=True, null=True)
    Telephone_Number = models.CharField(max_length=60, blank=True, null=True)
    Date_Acquired = models.DateField(blank=True, null=True)
    CountryCode = models.CharField(max_length=25, blank=True, null=True)
    Industry = models.CharField(max_length=100, blank=True, null=True)
    DateEntered = models.DateField(blank=True, null=True)
    ClientType = models.CharField(max_length=5, blank=True, null=True)
    ModifiedBy = models.CharField(max_length=30, blank=True, null=True)
    AccountOfficer = models.CharField(max_length=100, blank=True, null=True)
    ContactPerson = models.CharField(max_length=100, blank=True, null=True)
    ClientOf = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.ClientName}"
    
class csv_casefolder(models.Model):
    clientnumber = models.CharField(max_length=25, blank=True, null=True)
    folder_description = models.CharField(max_length=200)


class csv_matter(models.Model):
    Client_Number = models.CharField(max_length=15, blank=True, null=True)
    ApplicationNo = models.CharField(max_length=25, blank=True, null=True)
    Case1 = models.CharField(max_length=250, blank=True, null=True)	
    Case2 = models.CharField(max_length=250, blank=True, null=True)
    Applicant =models.CharField(max_length=200, blank=True, null=True)
    ClientRefNo = models.CharField(max_length=60, blank=True, null=True)
    PatAppNo = models.CharField(max_length=30, blank=True, null=True)
    ApplicationDate	= models.DateField(null=True, blank=True )
    Serial_Number = models.CharField(max_length=30, blank=True, null=True)
    Serial_Date = models.DateField(null=True, blank=True )
    Certificate_Number = models.CharField(max_length=30, blank=True, null=True)
    RegistrationDate = models.DateField(null=True, blank=True )
    ApplicationStatus = models.CharField(max_length=30, blank=True, null=True)
    ApplicationType = models.CharField(max_length=30, blank=True, null=True) 
    CountryCode = models.CharField(max_length=30, blank=True, null=True)
    DocketNumber = 	models.CharField(max_length=30, blank=True, null=True)
    HandlingOfficer	= models.CharField(max_length=20, blank=True, null=True)
    BPTTTExaminer = models.CharField(max_length=30, blank=True, null=True)
    StageNo = models.CharField(max_length=30, blank=True, null=True)
    OGNumber = 	models.CharField(max_length=30, blank=True, null=True)
    DateOfPublish = models.DateField(null=True, blank=True )
    DateOfWithdrawn	= models.DateField(null=True, blank=True )
    WithIPC	= models.CharField(max_length=5, blank=True, null=True)
    IPCNumber	= models.CharField(max_length=30, blank=True, null=True)
    WithPriority = models.CharField(max_length=30, blank=True, null=True)	
    PriorityDate = models.DateField(null=True, blank=True )	
    PriorityNumber = models.CharField(max_length=30, blank=True, null=True) 	
    PriorityFiling = models.CharField(max_length=30, blank=True, null=True)
    Owner = models.CharField(max_length=15, blank=True, null=True)
    OGPGENO = models.CharField(max_length=10, null=True, blank=True)
    ExClaims = models.CharField(max_length=10, blank=True, null=True)
    NoOfClaims = models.CharField(max_length=15, blank=True, null=True)
    NewLaw	    = models.CharField(max_length = 5, blank=True, null=True)
    BasedOnLocal = models.CharField(max_length = 5, blank=True, null=True)
    ClientContactPerson	= models.CharField(max_length=60, blank=True, null=True)
    ClaimColor= models.CharField(max_length=60, blank=True, null=True)	
    PCTAppno = models.CharField(max_length=30, blank=True, null=True)	
    PCTFileDate	= models.DateField(null=True, blank=True )
    PCTPUBNum = models.CharField(max_length=30, blank=True, null=True)	
    PCTPUBDate = models.DateField(null=True, blank=True )	
    LngInterApplication = models.CharField(max_length=30, blank=True, null=True)	
    LngInterPublication	= models.CharField(max_length=30, blank=True, null=True)
    PriorityClaimed = models.CharField(max_length=5, blank=True, null=True)	
    PartnerInCharge	= models.CharField(max_length=5, blank=True, null=True)	
    ReasonOfWithdrawn = models.CharField(max_length=200, blank=True, null=True)		
    DivisionalApplication = models.CharField(max_length=30, blank=True, null=True)	
    DivisionalParent = models.CharField(max_length=30, blank=True, null=True)	
    Remarks = models.CharField(max_length=60, blank=True, null=True)	
    HandledByCPA = models.CharField(max_length=10, blank=True, null=True)	
    DateCreated = models.DateField(null=True, blank=True )	
    DateModified = models.DateField(null=True, blank=True )		
    CreatedBy = models.CharField(max_length=10, blank=True, null=True)
    ModifiedBy = models.CharField(max_length=10, blank=True, null=True)
    Madrid = models.CharField(max_length=10, blank=True, null=True)
    Renewal = models.CharField(max_length=1, blank=True, null=True)

    def __str__(self):
        return f"{self.Case1}"

class csv_AR(models.Model):
    Client_Number = models.CharField(max_length=15, blank=True, null=True)
    ApplicationNo = models.CharField(max_length=25, blank=True, null=True)
    BillNumber = models.CharField(max_length=10, blank=True, null=True)
    BillDate = models.DateField(null=True, blank=True)
    BillAmount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    PesoAmount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    EuroAmount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    PaymentTag = models.CharField(max_length=5, blank=True, null=True)
    ORNumber1 = models.CharField(max_length=10, blank=True, null=True) 	
    ORDate1	= models.DateField(null=True, blank=True)
    AmountPaid1	= models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    CheckNumber1 = models.CharField(max_length=30, blank=True, null=True)	
    CheckDate1 = models.DateField(null=True, blank=True)	
    ORNumber2 = models.CharField(max_length=10, blank=True, null=True)	
    ORDate2	= models.DateField(null=True, blank=True)
    AmountPaid2	= models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    CheckNumber2 = models.CharField(max_length=30, blank=True, null=True)		
    CheckDate2	= models.DateField(null=True, blank=True)
    ORNumber3 = models.CharField(max_length=10, blank=True, null=True)	
    ORDate3	= models.DateField(null=True, blank=True)
    AmountPaid3	= models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    CheckNumber3 = 	models.CharField(max_length=30, blank=True, null=True)		
    CheckDate3 = models.DateField(null=True, blank=True)	
    ContactPerson = models.CharField(max_length=60, blank=True, null=True)
    Remarks	= models.TextField(blank=True, null=True)
    DisCount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    PF = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)	
    FILINGFEES = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)	
    OPE = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    Vat	= models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    PesoRate = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    StampID = models.CharField(max_length=60, blank=True, null=True)	
    ModifiedBy = models.CharField(max_length=60, blank=True, null=True)	


class csv_task(models.Model):
    ClientNo = models.CharField(max_length=15, null=True, blank=True)
    ApplicationNo = models.CharField(max_length=25, blank=True, null=True)
    ActivityDate = models.DateField(null=True, blank=True)
    seqno = models.CharField(max_length=20, blank=True, null=True)
    TaskCode = models.CharField(max_length=15, blank=True, null=True)
    TranType = models.CharField(max_length=10, blank=True, null=True)
    DocumentCode = models.CharField(max_length=10, blank=True, null=True)
    BillDate = models.DateField(null=True, blank=True)
    TaskDescription = models.TextField(blank=True, null=True)
    DocumentType = models.CharField(max_length=10, blank=True, null=True)
    ActionType = models.CharField(max_length=10, blank=True, null=True)
    CaseOfficer = models.CharField(max_length=10, blank=True, null=True)
    Billed = models.CharField(max_length=10, blank=True, null=True)
    ContactPerson = models.CharField(max_length=60, blank=True, null=True)
    StageNo = models.CharField(max_length=10, blank=True, null=True)
    MailOut = models.CharField(max_length=10, blank=True, null=True)
    MailSent = models.CharField(max_length=10, blank=True, null=True)
    DocumentPath = models.CharField(max_length=100, blank=True, null=True)
    IpoFilingDate = models.DateField(null=True, blank=True)
    GroupCode = models.CharField(max_length=100, blank=True, null=True)
    LetterToClient = models.CharField(max_length=10, blank=True, null=True)
    LetterToIPO = models.CharField(max_length=10, blank=True, null=True)
    StampID = models.CharField(max_length=60, blank=True, null=True)
    ModifiedBy = models.CharField(max_length=60, blank=True, null=True)
    PaperNo = models.CharField(max_length=10, blank=True, null=True)

class egazette(models.Model):
    Application_Number = models.CharField(max_length=25, null=True, blank=True)
    Filing_Date = models.CharField(max_length=40, null=True, blank=True)
    Mark = models.CharField(max_length=150, blank=True, null=True)	
    Applicant = models.CharField(max_length=150, blank=True, null=True)	
    Nice_class = models.CharField(max_length=150, blank=True, null=True)

    def __str__(self):
        return f"{self.Application_Number} - {self.Mark}"

class csv_duedates(models.Model):

    ClientNo = models.CharField(max_length=15, null=True, blank=True)
    ApplicationNo = models.CharField(max_length=25, blank=True, null=True)
    DueDates = models.DateField(null=True, blank=True)
    DueCode = models.CharField(max_length=15, blank=True, null=True)
    Activities = models.TextField(blank=True, null=True)
    ReferenceNumber = models.CharField(max_length=60, blank=True, null=True)
    Done = models.CharField(max_length=5, blank=True, null=True)
    ActionDate = models.DateField(null=True, blank=True)
    Complied = models.CharField(max_length=5, blank=True, null=True)
    DateComplied = models.DateField(null=True, blank=True)
    Remarks = models.TextField(blank=True, null=True) 
# reference tables

class csv_apptype(models.Model):
    ApplicationType = models.CharField(max_length=10, null=True, blank=True)
    Description = models.CharField(max_length=100, blank=True)

class csv_appstat(models.Model):
    AppStat = models.CharField(max_length=10, blank=True)
    ApplicationStatus = models.CharField(max_length=50, blank=True)

class csv_officers(models.Model):
    CaseOfficers = models.CharField(max_length=10, blank=True, null=True)
    OfficerName = models.CharField(max_length=100, blank=True, null=True)

class csv_docs(models.Model):
    DocumentType = models.CharField(max_length=10, blank=True)
    Description = models.CharField(max_length=100)

class csv_applicant(models.Model):
    ApplicantCode = models.CharField(max_length=200, blank=True)
    ApplicantName = models.CharField(max_length=200, blank=True)

class csv_templates(models.Model):
    DocumentCode = models.CharField(max_length=20, blank=True)
    Description = models.CharField(max_length=200, blank=True)
    ApplicationType = models.CharField(max_length=10, blank=True)
    DocPath = models.CharField(max_length=100, blank=True)

class csv_industry(models.Model):
    Industry = models.CharField(max_length=10, blank=True)
    Description = models.CharField(max_length=200, blank=True)

class csv_stages(models.Model):
    Stage = models.IntegerField(null=True, blank=True)
    Description = models.CharField(max_length=200, blank=True)

class csv_clientfile(models.Model):
    id = models.IntegerField(primary_key=True)
    client_number = models.CharField(max_length=15, null=True)
    entity_type = models.CharField(max_length=15, blank=True, null=True)
    category = models.CharField(max_length=15, blank=True, null=True)
    client_name = models.CharField(max_length=200, blank=True, null=True)
    unit_description = models.CharField(max_length=60, blank=True, null=True)
    street = models.CharField(max_length=60, blank=True, null=True)
    city = models.CharField(max_length=60, blank=True, null=True)
    state = models.CharField(max_length=60, blank=True, null=True)
    country_name = models.CharField(max_length=60, blank=True, null=True)
    fax_number = models.CharField(max_length=60, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    website = models.CharField(max_length=60, blank=True, null=True)
    zip_code = models.CharField(max_length=30, blank=True, null=True)
    landline = models.CharField(max_length=100, blank=True, null=True)
    date_acquired = models.DateField(null=True, blank=True)
    country = models.CharField(max_length=10, blank=True, null=True)
    industry_id = models.IntegerField(null=True, blank=True)
    date_entered =  models.DateField(null=True, blank=True)
    client_type = models.CharField(max_length=10, blank=True, null=True)
    account_officer = models.CharField(max_length=50, blank=True, null=True)
    account_person = models.CharField(max_length=50, blank=True, null=True)



