from django.shortcuts import render, HttpResponse
import requests
# Create your views here.

def luminosity(request):
    if 'value' in request.GET:
       value = request.GET['value']

       if value:
           args = {'type': 'lux', 'value': value}
           response = requests.post('https://pi1-eafit-dgarciag.azurewebsites.net/luminositys/', args)
           luminosity_json = response.json()

    response = requests.get('https://pi1-eafit-dgarciag.azurewebsites.net/luminositys/')
    luminositys = response.json()
    return render(request, "luminosity.html", {'luminositys': luminositys})