from .serializer import LoginSerializer, RegisterSerializer,UserSerializer
from django.contrib.auth.models import User
from knox.models import AuthToken
from rest_framework import viewsets,generics,permissions
from rest_framework.response import Response
from knox.auth import TokenAuthentication
from django.contrib.auth import login
from django.contrib.auth.hashers import make_password
from rest_framework.exceptions import AuthenticationFailed
from rest_framework import status


class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    def post(self,request,*args, **kwargs):
        serializer = self.get_serializer(data = request.data)
        if serializer.is_valid():
            password = make_password(request.data["password"])
            user = serializer.save(password=password)
            return Response({"user" : serializer.data , 'token' : AuthToken.objects.create(user)[1]}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginAPI(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self,request):
        serializer = self.get_serializer(data = request.data)
        print(request.data)
        serializer.is_valid(raise_exception = True)
        user = serializer.validated_data

        print(user)
        _,token = AuthToken.objects.create(user)

        return Response({
            "user" : UserSerializer(user, context=self.get_serializer_context()).data,
            "token" : token
        })