from rest_framework import serializers
from django.core.exceptions import (
    ValidationError,
)
import django.contrib.auth.password_validation as validators
from Accounts.models import Account
import json

USER_ROLES_CHOICE = (
    ("1", 'Customer'),
    ("2", 'Salon')
)


class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(
        style={'input_type': 'password'}, write_only=True)
    role = serializers.ChoiceField(
        choices=USER_ROLES_CHOICE)

    class Meta:
        model = Account
        fields = ['email', 'username', 'role', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    # def validate_password(self, data):
    #     """
    #     validates password by django password validators.
    #     """
    #     print(self.instance)
    #     validators.validate_password(data, self.instance)
    #     return data

    def save(self):
        account = Account(
            email=self.validated_data['email'],
            username=self.validated_data['username']
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        if password != password2:
            raise serializers.ValidationError(
                {'password': ['Passwords must match.']})
        try:
            validators.validate_password(password, account)
        except ValidationError as error:
            error_msg = []
            for i in error:
                error_msg.append(i)
            raise serializers.ValidationError({'password': error_msg})
        print(account)
        account.set_password(password)
        print(self.validated_data['role'])
        if USER_ROLES_CHOICE[0][0] == str(self.validated_data['role']):
            account.is_customer = True
        elif USER_ROLES_CHOICE[1][0] == str(self.validated_data['role']):
            account.is_salon = True
        account.save()
        return account
