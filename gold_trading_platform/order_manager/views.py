from django.http import HttpResponse
from django.shortcuts import render
from django.db import connection
from datetime import datetime
from django.utils.datastructures import MultiValueDictKeyError

today = datetime.today()


# Create your views here.
def add_to_cart(request):
    try:
        if request.method == 'GET':
            order_id = get_last_order_id() + 1
            quantity = int(request.GET['quantity'])
            #price = request.GET['price']
            #print(price)
            sql_command = "INSERT INTO Orders VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            val = (order_id, quantity, 3.99, today, 1, 'sent', 0, 1)

            cursor = connection.cursor()
            cursor.execute(sql_command, val)

            return HttpResponse('<h1>Ordered</h1>')
        else:
            return HttpResponse('not ordered')
    except MultiValueDictKeyError:
        return HttpResponse('MultiValueDictKeyError')


# GETTING THE LAST ORDER_ID
def get_last_order_id():
    cursor = connection.cursor()
    cursor.execute("""SELECT order_id FROM Orders ORDER BY order_id DESC""")
    order_id = str(cursor.fetchone()).replace(',', '')
    order_id = order_id.translate(str.maketrans(dict.fromkeys("[('')]")))

    if order_id == 'None':
        return 0
    else:
        return int(order_id)

