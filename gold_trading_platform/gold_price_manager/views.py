import datetime
import json
import urllib.request
import http.client
import mimetypes
from http.client import InvalidURL
from urllib.error import HTTPError
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
"""
We return the values based on the base currency. For example, for 1 USD the return is a number like 0.000634 
for Gold (XAU).To get the gold rate per troy ounce in USD: 1/0.000634= 1577.28 USD
"""


def get_gold_rate(request):
    try:
        conn = http.client.HTTPSConnection("www.goldapi.io")
        payload = ''
        headers = {
            'x-access-token': 'goldapi-eaivajsksdud524-io',
            'Content-Type': 'application/json'
        }
        conn.request("GET", "/api/XAU/USD", payload, headers)
        res = conn.getresponse().read()
        data_list = str(res).split(",")
        data = {
            "metal": data_list[1][9:-1],
            "currency": data_list[2][12:-1],
            "prev_close_price": data_list[5][19:],
            "open_price": data_list[6][13:],
            "low_price": data_list[7][12:],
            "high_price": data_list[8][13:],
            "price": data_list[10][8:],
            "ask": data_list[13][6:],
            "bid": data_list[14][6:-2],
        }
        return render(request, 'gold_price_manager/product.html', data)
    except ConnectionAbortedError:
        return HttpResponse('[WinError 10053] Une connexion établie a été abandonnée par un logiciel de votre ordinateur hôte')



