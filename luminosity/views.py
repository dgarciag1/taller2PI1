from django.shortcuts import render, HttpResponse
import requests
# Create your views here.
def luminosity(request):
    if 'value' in request.GET:
            value = request.GET['value']

            if value:

                args = {'type': 'lux', 'value': value}
                response = requests.post('http://127.0.0.1:8000/luminositys/', args)
                luminosity_json = response.json()

    response = requests.get('http://127.0.0.1:8000/luminositys/')
    luminositys = response.json()
    return render(request, "luminosity.html", {'luminositys': luminositys})