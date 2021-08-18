import json
import urllib

from django.utils.datastructures import MultiValueDictKeyError
from django.http import HttpResponse
from django.shortcuts import render
from django.db import connection
from .models import User


# Create your views here.

# AUTHENTICATION PAGE
def index(request):
    return render(request, 'user_connection_manager/index.html')


def get_profile(request):
    return render(request, 'user_connection_manager/user_profile.html')

# GETTING USERS FROM DB
def get_users_db():
    username_list = []
    password_list = []

    cursor = connection.cursor()
    cursor.execute("""SELECT username, password, type FROM User """)
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
        get_taken_username()
        for key, value in user.items():
            if username == key and password == value:
                connected = True
                break

        if connected:
            return render(request,'user_connection_manager/admin_dashboard.html')
        else:
            return HttpResponse('<h1>Wrong username or password</h1>')

    except MultiValueDictKeyError:
        return HttpResponse('MultiValueDictKeyError')


# GETTING THE LAST USER_ID
def get_last_user_id():
    cursor = connection.cursor()
    cursor.execute("""SELECT user_id FROM User ORDER BY user_id DESC""")
    user_id = str(cursor.fetchone()).replace(',', '')
    user_id = user_id.translate(str.maketrans(dict.fromkeys("[('')]")))
    return int(user_id)


# GETTING THE USERNAME FROM DB
def get_taken_username():
    username_list = []
    cursor = connection.cursor()
    cursor.execute("""SELECT username FROM User ORDER BY user_id DESC""")
    data = str(cursor.fetchall())
    data = data.translate(str.maketrans(dict.fromkeys("[('')]")))
    username_list = data.split(',')
    return username_list


# CHECK IF USERNAME ALREADY EXIST
def check_if_username_taken(username, username_list):
    taken = False
    for user_name in username_list:
        if user_name == username:
            taken = True

    return taken


# REGISTRATION FUNCTION
def register(request):
    try:
        user_id = get_last_user_id() + 1
        sql_command = "INSERT INTO User (user_id, username, password, email) " \
                      "VALUES (%s, %s, %s, %s)"
        username = request.GET['username']
        email = request.GET['email']
        password = request.GET['password']
        confirm_password = request.GET['confirm_pass']

        if check_if_username_taken(username, get_taken_username()):
            return HttpResponse('<h1>Username Already Taken</h1>')
        elif password == confirm_password:
            val = (user_id, username, password, email)
            cursor = connection.cursor()
            cursor.execute(sql_command, val)
            return HttpResponse('<h1>Registered</h1>')
        else:
            return HttpResponse('<h1>passwords do not match</h1>')

    except MultiValueDictKeyError:
        return HttpResponse('<h1>MultiValueDictKeyError</h1>')


