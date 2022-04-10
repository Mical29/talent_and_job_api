from django.db import models
from account.models import Account

# Create your models here.

class Job(models.Model):
    jobTitle = models.CharField(max_length=150)
    jobDescription = models.CharField(max_length=500)
    necessarySkills = models.CharField(max_length=500)

    def __str__(self):
        return self.jobTitle

class UserAppliedJob(models.Model):
    test = models.CharField(max_length=2,default=None,null=True,blank=True)
    job_id = models.ForeignKey(Job,on_delete=models.CASCADE,null=True,related_name='job')
    user_id = models.ForeignKey(Account,on_delete=models.CASCADE,null=True,related_name='user')
    
    def __str__(self):
        return str(self.user_id) + "-->" +str(self.job_id)