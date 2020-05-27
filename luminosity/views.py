from django.shortcuts import render, HttpResponse
import requests
# Create your views here.
def luminosity(request):
    if 'value' in request.GET:
            value = request.GET['value']

            if value:

                args = {'type': 'lux', 'value': value}
                response = requests.post('http://pi1-eafit-dgarciag-fr.azurewebsites.net/luminositys/', args)
                luminosity_json = response.json()

    response = requests.get('http://pi1-eafit-dgarciag-fr.azurewebsites.net/luminositys/')
    luminositys = response.json()
    return render(request, "luminosity.html", {'luminositys': luminositys})