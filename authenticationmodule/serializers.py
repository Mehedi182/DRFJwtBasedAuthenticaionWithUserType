from rest_framework import serializers
from django.contrib.auth.models import User
from .models import PartyUser
from .enums import E_UserType


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)   # write only password not show in response
    user_type = serializers.IntegerField()

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
        )
        if validated_data['user_type'] == E_UserType.Admin.value:
            user.is_staff = True
            user.save()
        PartyUser.objects.create(
            user=user,
            type=validated_data['user_type']
        )
        """
        we remove user_type field otherwise it will give attribute error. 
        because this is not in user table
        """
        self.fields.pop("user_type")
        return user

    class Meta:
        model = User
        fields = ("id", "username", "password", "email", "user_type")


class PartyUserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = PartyUser
        fields = ('type', )


class UserListSerializer(serializers.ModelSerializer):

    party = PartyUserListSerializer

    class Meta:
        model = User
        fields = ("id", "username", "password", "email", "party")



