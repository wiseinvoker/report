# coding=utf-8
from django.shortcuts import render
from rest_framework import generics, permissions, filters, viewsets
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework import serializers

from .models import Report
from .serializers import ReportSerializer, AccountSerializer, ReportsListSerializer

import json

from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.models import User
from django.middleware.csrf import get_token
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from rest_framework import permissions, status, views, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class ReportViewSet(viewsets.ModelViewSet):
	queryset = Report.objects.all()
	serializer_class = ReportSerializer
	filter_backends = (filters.SearchFilter,filters.DjangoFilterBackend,)
	filter_fields = ('reporter', 'created', )

class ReportListViewSet(viewsets.ModelViewSet):
	permission_classes = (permissions.IsAdminUser,)
	queryset = Report.objects.all()
	serializer_class = ReportsListSerializer
	filter_backends = (filters.SearchFilter, filters.DjangoFilterBackend, filters.OrderingFilter, )
	ordering_fields = ('reporter')
	ordering = ('reporter',)
	filter_fields = ('created', )


# User Authentication view
class LoginView(views.APIView):
	
	# renderer_classes = (JSONPRenderer, JSONRenderer)

	def post(self, request, format=None):
		
		data = json.loads(request.body.decode())
		# data = request.POST
		username = data.get('username', None)
		password = data.get('password', None)

		account = authenticate(username=username, password=password)
		
		if account is not None:
			if account.is_active:
				login(request, account)
				serialized = AccountSerializer(account)
				# serialized.data.token = get_token(request)
				# serialized.data.session_id = request.session.session_key
				resp = Response(serialized.data)
				resp['csrftoken'] = get_token(request)
				# resp['session_id'] = request.session.session_key
				return resp
		else:
			return Response({
				'status': 'Unauthorized',
				'message': 'This account has been disabled.',
				}, status=status.HTTP_401_UNAUTHORIZED)

class LogoutView(views.APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, format=None):
        logout(request)

        return Response({}, status=status.HTTP_204_NO_CONTENT)

class ProfileView(views.APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, format=None):
        serialized = AccountSerializer(request.user)
        resp = Response(serialized.data)
        resp['csrftoken'] = get_token(request)
        return resp

    def put(self, request, format=None):
    	current_user = request.user
    	password = request.data['password']
    	confirm_password = request.data['confirm_password']
    	if password and confirm_password and password == confirm_password:
    		current_user.set_password(password)
    		current_user.save()
    	serialized = AccountSerializer(current_user)
    	resp = Response(serialized.data)
    	resp['csrftoken'] = get_token(request)
    	return resp

