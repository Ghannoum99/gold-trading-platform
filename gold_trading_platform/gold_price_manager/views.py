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
def get_gold_rate(request):
    if request.method == 'POST':
        conn = http.client.HTTPSConnection("www.metals-api.com")
        conn.request("GET", "/api/latest?base=USD&symbols=XAU,XAG&access_key=cnxyo0nz7fq2qym0qui4lok0tys759229pav5v13ve37deemnsvqinli1530")
        res = conn.getresponse().read()
        data_list = str(res).split(",")

        """
        We return the values based on the base currency. For example, for 1 USD the return is a number like 0.000634 
        for Gold (XAU).To get the gold rate per troy ounce in USD: 1/0.000634= 1577.28 USD
        """

        data = {
            "date": data_list[2][8:-1],
            "base": data_list[3][8:-1],

        }
    else :
        data = {}

    return render(request, 'gold_price_manager/home.html', data)

