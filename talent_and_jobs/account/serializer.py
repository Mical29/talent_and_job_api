from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .models import Account
from collections import OrderedDict
from django.contrib.auth.hashers import make_password

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'

        extra_kwargs = {
            'password': {'write_only': True}
        }



class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        # fields = ('id', 'user_name', 'email', 'password')
        fields = ('username','email','password')
        extra_kwargs = {'password': {'write_only': True}}

        def create(self,validated_data):
            # print("User Created and password is")
            # print(validated_data["password"])
            # print(make_password(validated_data["password"]))
            user = Account(username=validated_data["username"],email=validated_data["email"],is_active=validated_data["is_active"],password=make_password(validated_data["password"]))
            user.save()
            return user


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, data):
        username = Account.objects.get(email=data["email"]).username
        password = data["password"]
        newData = OrderedDict()
        newData["username"] = username
        newData["password"] = make_password(data["password"])
        # print(data)
        # print(newData)
        user = authenticate(**data)
        print(user)
        if user and user.is_active:
            # print("it work")
            # print(user)
            return user
        # print(serializers.ValidationError("Invalid Details"))
        raise serializers.ValidationError("Invalid Details.")
