from django.shortcuts import render
from django.http import HttpResponse

# Index view
def index(request):
    return HttpResponse("Hi")
