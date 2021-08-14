from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

# AUTHENTICATION PAGE
def index(request):
    return render(request, 'user_connection_manager/index.html')


def login(request):
    username = request.GET['username']
    password = request.GET['password']
    print('hi')

    if username == 'admin' and password == '123':
        return HttpResponse('Hello')