from dataclasses import field
from account.serializer import UserSerializer
from rest_framework import serializers
from .models import Job,UserAppliedJob
from account.models import Account


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = '__all__'


class UserAppliedJobSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAppliedJob
        fields = '__all__'


class UserAppliedJobSerializer(serializers.ModelSerializer):
    job_id = JobSerializer(required=True)
    user_id = UserSerializer(required=True)
    class Meta:
        model = UserAppliedJob
        fields = ('job_id','user_id')