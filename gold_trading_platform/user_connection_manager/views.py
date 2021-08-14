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


# GETTING THE LAST USER_ID
def get_last_user_id():
    cursor = connection.cursor()
    cursor.execute("""SELECT user_id FROM User ORDER BY user_id DESC""")
    user_id = str(cursor.fetchone()).replace(',', '')
    user_id = user_id.translate(str.maketrans(dict.fromkeys("[('')]")))
    return int(user_id)


# REGISTRATION FUNCTION
def register(request):
    try:
        user_id = int(get_last_user_id()) + 1
        sql_command = "INSERT INTO User VALUES (2, %s, %s, %s)"
        username = request.GET['username']
        email = request.GET['email']
        password = request.GET['password']
        password_confirmation = request.GET['password_conf']

        if password == password_confirmation:
            val = (username, password, email)
            cursor = connection.cursor()
            cursor.execute(sql_command, val)
            return HttpResponse('<h1>Registered</h1>')
        else:
            return HttpResponse('passwords do not match')

    except MultiValueDictKeyError:
        return HttpResponse('MultiValueDictKeyError')


