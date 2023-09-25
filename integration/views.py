import requests
from django.http import HttpResponse

from savon_test.settings import env

headers = {'Authorization': 'Bearer %s' % (env('EFECTE_TOKEN'))}


# Create your views here.

def index(request):
    return HttpResponse('welcome');


def test_api(request):
    print(headers.get('Authorization'))
    response = requests.get(env('EFECTE_URL') + '/dc', headers=headers)
    return HttpResponse(response)


def echo(request):
    response = requests.get(env('EFECTE_URL') + '/echo')
    return HttpResponse(response)
