from django.urls import path, include

from rest_framework import routers
from .api import JobLists,CreateJob,DeleteJob,UpdateJob,UserAppliedJob,UserApliedJobList

router = routers.DefaultRouter()


urlpatterns = [
    path('api/jobs/', JobLists.as_view()),   
    path('api/jobs/create', CreateJob.as_view()),   
    path('api/jobs/delete', DeleteJob.as_view()),  
    path('api/jobs/update', UpdateJob.as_view()),  
    path('api/jobs/appliedjob', UserApliedJobList.as_view()), 
    path('api/jobs/userappliedjobs/apply', UserAppliedJob.as_view()),     
]