from urllib import response
from rest_framework.test import APITestCase
from rest_framework import status
import json
from django.urls import reverse
from .serialisers import JobSerializer
from .models import Job

class CreateJob(APITestCase):
    
    def test_create_job(self):
        data = {"jobTitle" : "Test Job Title" , "jobDescription" : "loream ipsum", "necessarySkills" : "Test"}
        response = self.client.post("http://127.0.0.1:8000/talent_and_job/api/jobs/create",data)
        self.assertEqual(response.status_code , status.HTTP_201_CREATED)
