from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from .models import Image
import json
from django.contrib.auth import authenticate

# Create your views here.
@csrf_exempt
def index(request):
    images_list = Image.objects.all()
    return HttpResponse(serializers.serialize("json", images_list))

@csrf_exempt
def add_user_view(request):
    if request.method == 'POST':
        json_user = json.loads(request.body)
        username = json_user['username']
        first_name = json_user['first_name']
        last_name = json_user['last_name']
        password = json_user['password']
        email = json_user['email']

        user_model = User.objects.create_user(username=username, password=password)
        user_model.first_name = first_name
        user_model.last_name = last_name
        user_model.email = email
        user_model.save()
    return HttpResponse(serializers.serialize("json", [user_model]))

@csrf_exempt
def show_public_images_user(request, user_id):
    images_list = Image.objects.filter(user=user_id, is_public=True)
    return HttpResponse(serializers.serialize("json", images_list))

@csrf_exempt
def login(request):
    if request.method == 'POST':
        json_user = json.loads(request.body)
        username = json_user['username']        
        password = json_user['password']
        
        user = authenticate(username=username, password=password)
        if user is not None:
            return HttpResponse(status=200)
        else:
            return HttpResponse(status=401)
        
    return HttpResponse(status=405)

@csrf_exempt
def update_user(request):
    return HttpResponse('[{"fields": {"username": "XXXX"}}]')