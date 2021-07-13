from django.http import HttpResponse
from django.shortcuts import render


def hello_world(requests):
    return HttpResponse('Hello world!')
