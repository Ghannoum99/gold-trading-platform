from django.http import HttpResponse
from django.shortcuts import render
from django.db import connection


# Create your views here.

# AUTHENTICATION PAGE
from django.utils.datastructures import MultiValueDictKeyError


def index(request):
    return render(request, 'user_connection_manager/index.html')


# GETTING USERS FROM DB
def get_users_db():
    pass


# LOGIN FUNCTION
def login(request):
    try:
        username_list = []
        password_list = []

        username = request.GET['username']
        password = request.GET['password']

        cursor = connection.cursor()
        data = cursor.execute("""SELECT username, password FROM User """)
        
        for row in data:
            username_list.append(row[0])
            password_list.append(row[1])

        user = dict(zip(username_list, password_list))

        for key, value in user.items():
            if username == key and password == value:
                return HttpResponse('<h1>Connected<h1>')
            else:
                return HttpResponse('Wrong username or password')
    except MultiValueDictKeyError:
        return HttpResponse('MultiValueDictKeyError')


# REGISTRATION FUNCTION
def register(request):
    pass

