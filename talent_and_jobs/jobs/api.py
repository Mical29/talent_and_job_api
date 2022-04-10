from account.models import Account
from rest_framework import viewsets, permissions,generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Job
from .models import UserAppliedJob as UJ
from .serialisers import JobSerializer,UserAppliedJobSerializer

class JobLists(APIView):
    
    def get(self,request,*args,**kwargs):
        jobs = Job.objects.all()
        serializer = JobSerializer(jobs,many=True)
        return Response(serializer.data)
        

class CreateJob(APIView):
    
    def post(self,request,*args, **kwargs):
        serializer = JobSerializer(data=request.data)
        if serializer.is_valid():
            job = serializer.save()
            return Response({"message" : "200 success : Job Created Successfully"})

class DeleteJob(APIView):

    def delete(self,request,*args, **kwargs):
        job_id = request.data['id']
        job = Job.objects.filter(id = job_id)
        if job.exists():
            job.delete()
            return Response({"message" : "200 success : Job Deleted Successfully"})
        else:
            return Response({"message" : "400 success : Job is not exist"})

class UpdateJob(APIView):
    def patch(self,request,*args, **kwargs):
        job_id = request.data['id']
        job = Job.objects.filter(id = job_id)
        if job.exists():
            Job.objects.filter(id = job_id).update(jobTitle = request.data['jobTitle'],jobDescription= request.data['jobDescription'],necessarySkills = request.data['necessarySkills'])
            return Response({"message" : "200 success : Job Update Successfully"})
        else:
            return Response({"message" : "400 success : Job is not exist"})

class UserAppliedJob(APIView):
    def post(self,request,*args, **kwargs):
        job = Job.objects.filter(id = request.data['jobid'])
        user = Account.objects.filter(id = request.data['userid'])
        UJ.objects.create(job_id=job,user_id=user)
        
        return Response({"message" : "Successfully Applied Job"})

class UserApliedJobList(APIView):
    def get(self,request,*args, **kwargs):
        users = UJ.objects.all()
        serializer = UserAppliedJobSerializer(users,many=True)
        return Response(serializer.data)