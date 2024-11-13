# Uncomment the required imports at the top
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import logout
from django.contrib import messages
from datetime import datetime

from django.http import JsonResponse
from django.contrib.auth import login, authenticate
import logging
import json
from django.views.decorators.csrf import csrf_exempt

# Get an instance of a logger
logger = logging.getLogger(__name__)

# Create your views here.

# Create a `login_request` view to handle sign in request
@csrf_exempt
def login_user(request):
    if request.method == 'POST':
        # Get username and password from request body
        data = json.loads(request.body)
        username = data['userName']
        password = data['password']
        # Try to authenticate the user
        user = authenticate(username=username, password=password)
        data = {"userName": username}
        if user is not None:
            # Login the user if authentication succeeds
            login(request, user)
            data = {"userName": username, "status": "Authenticated"}
        else:
            data = {"userName": username, "status": "Failed"}
        return JsonResponse(data)
