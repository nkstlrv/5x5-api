from django.shortcuts import render
from django.http import JsonResponse


def index(request):
    data = {"message": "Hello World"}
    return JsonResponse(data)
