import requests
import json
from django.shortcuts import render


def home(request):

    price_request = requests.get(
        "https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,ETH,CHZ,BNB,SOL,XRP,LUNA,ADA,DOGE,DOT,AVAX,SHIB,ATOM,LTC,TRX,ETC,ALGO,XLM,UNI,MANA,FTM,THETA,BTT,NEO,HOT,DENT,XVG,ETP,ZEN,UMA&tsyms=USD")
    price = json.loads(price_request.content)

    return render(request, 'home.html', {'price': price})
