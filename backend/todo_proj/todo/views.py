from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
from django.views import View
from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.decorators import action
from rest_framework.parsers import JSONParser
from rest_framework import status
from todo.models import *
from todo.serializers import *
import json
# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.filter(is_superuser=0).order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

@method_decorator(csrf_exempt, name='dispatch')
class TODOView(View):
    '''
        TODO View
    '''
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(TODOView, self).dispatch(request, *args, **kwargs)

    def get_object(self, pk):
        try:
            return TODO.objects.get(pk=pk)
        except TODO.DoesNotExist:
            raise Http404
    def get(self, request):
        queryset = TODO.objects.filter(user=request.user).order_by('-id')
        serializer = TODOSerializer(queryset, many=True)
        return HttpResponse(json.dumps(serializer.data))

    @method_decorator(csrf_exempt, name='dispatch')
    def post(self, request):
        request_data = json.loads(request.body)
        request_data['user'] = id=request.user.id
        serializer = TODOSerializer(data=request_data)
        if serializer.is_valid():
            serializer.save()
        return JsonResponse(serializer.data)

    def put(self, request, pk, format=None):
        todo = self.get_object(pk)
        request_data = json.loads(request.body)
        request_data['user'] = id=request.user.id
        serializer = TODOSerializer(todo, data=request_data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        todo = self.get_object(pk)
        todo.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)

@method_decorator(csrf_exempt, name='dispatch')
class Userstatus(View):

    def post(self, request):
        if request.user.is_authenticated:
            data = {'username': request.user.username, 'first_name': request.user.first_name, 'status': 1, "message": "Success"}
            return HttpResponse(json.dumps(data), status=200)
        else:
            data = {'status': 0, 'message': 'Invalid User'}
            return HttpResponse(json.dumps(data), status=403)


@method_decorator(csrf_exempt, name='dispatch')
class user_login(View):
    def post(self, request):
        data = json.loads(request.read())
        res_data = {'username': '', 'status': 0}
        user = authenticate(username=data['username'], password=data['password'])
        if user:
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            res_data['username'] = user.username
            res_data['status'] = 1
            return HttpResponse(json.dumps(res_data))
        return HttpResponse(json.dumps(res_data), status=403)


@method_decorator(csrf_exempt, name='dispatch')
class user_logout(View):
    def get(self, request):
        resp_data = {'success': 1, 'message': "Logged Out"}
        logout(request)
        return HttpResponse(json.dumps(resp_data), status=200)
