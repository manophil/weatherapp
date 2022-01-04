from django.conf.urls import url
from django.shortcuts import render
import json
import urllib.request

# Create your views here.
api_key = '61db93d01a42d08548ccf4dd3e621e3e'


def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        res = urllib.request.urlopen(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}').read()
        json_data = json.loads(res)
        data = {
            "country_code":str(json_data['sys']['country']),
            "coordinate":str(json_data['coord']['lon']) +'  '+ str(json_data['coord']['lat']),
            "temp":str(json_data['main']['temp']) + 'k',
            "pressure":str(json_data['main']['pressure']),
            "humidity":str(json_data['main']['humidity']),




        }
    
    else:
        data = {}

    return render(request,'index.html', {'city':city, 'data':data})