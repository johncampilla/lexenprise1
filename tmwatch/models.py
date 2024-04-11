from django.db import models

class tmwatchexcemptions(models.Model):
    word = models.CharField(max_length=5, blank=True, null=True)

    def __str__(self):
        return f"{self.word}"
    
class TMwatchResult(models.Model):
    Application_Number = models.CharField(max_length=25, null=True, blank=True)
    Filing_Date = models.CharField(max_length=40, null=True, blank=True)
    Mark = models.CharField(max_length=150, blank=True, null=True)
    Applicant = models.CharField(max_length=150, blank=True, null=True)
    Nice_class = models.CharField(max_length=150, blank=True, null=True)
    my_account_id = models.IntegerField(null=True, blank=True)
    myClient_Number = models.CharField(max_length=15, blank=True, null=True)
    myApplicationNo = models.CharField(max_length=25, blank=True, null=True)
    myPatAppNo = models.CharField(max_length=30, blank=True, null=True)
    myApplicationDate = models.DateField(null=True, blank=True )
    myApplicant =models.CharField(max_length=200, blank=True, null=True)
    myClientRefNo = models.CharField(max_length=60, blank=True, null=True)
    myCase1 = models.CharField(max_length=250, blank=True, null=True)	

    def __str__(self):
        return f"{self.Application_Number}"
