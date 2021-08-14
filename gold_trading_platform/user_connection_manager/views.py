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
    username_list = []
    password_list = []
    cursor = connection.cursor()
    cursor.execute("""SELECT username, password FROM User """)
    data = cursor.fetchall()

    for row in data:
        username_list.append(row[0])
        password_list.append(row[1])

    user = dict(zip(username_list, password_list))
    return user


# LOGIN FUNCTION
def login(request):
    try:
        connected = False
        user = get_users_db()

        username = request.GET['username']
        password = request.GET['password']

        for key, value in user.items():
            if username == key and password == value:
                connected = True
                break

        if connected:
            return HttpResponse('<h1>Connected</h1>')
        else:
            return HttpResponse('<h1>Wrong username or password</h1>')

    except MultiValueDictKeyError:
        return HttpResponse('MultiValueDictKeyError')


# REGISTRATION FUNCTION
def register(request):
    pass

