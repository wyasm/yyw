from django.shortcuts import render
from django.http import JsonResponse


def login(request):
    # if request.method == "POST":
    data = {
        'status_code': 200
    }

    return JsonResponse(data=data)