# coding=utf-8
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Report
from django.contrib.auth import update_session_auth_hash

class AccountSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=False)
    confirm_password = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'is_superuser', 'is_staff', 'last_login', 
            'date_joined', 'first_name', 'last_name', 'password', 'confirm_password')
        read_only_fields = ('last_login', 'date_joined')



class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = ('id', 'reporter', 'task', 'learning', 'plan', 'data', 'outing', 'other', 'suggestion', 'created', 'updated')

class ReportsListSerializer(serializers.ModelSerializer):
    reporter = AccountSerializer(many=False)
    class Meta:
        model = Report
        fields = ('id', 'reporter', 'task', 'learning', 'plan', 'data', 'outing', 'other', 'suggestion', 'created', 'updated')

