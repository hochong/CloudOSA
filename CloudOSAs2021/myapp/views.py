from django.http import HttpResponse
from django.shortcuts import render
import requests
import json
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
def home(request):
    # return home page
    return render(request, 'CloudOSAs2021/home.html')


def terminal(request):
    # return terminal page
    return render(request, 'CloudOSAs2021/terminal.html')


def onetrace(request):
    r = requests.get('http://flaskosa.herokuapp.com/cmd/TRACE')

    try:
        response = {
            'content': json.loads(r.content.decode())
        }
        print(json.loads(r.content.decode()).keys())
        print(response['content']['yunits'])
        print(response['content']['xunits'])
        j = json.loads(r.content.decode())
        for key in j.keys():
            if key != 'ydata' and key != 'xdata':
                print(key + ': ' + str(j[key]))

        return render(request, 'CloudOSAs2021/plotchart.html', response)
    # handle random string
    except json.decoder.JSONDecodeError as e:
        print(e)
        return render(request, 'CloudOSAs2021/plotchart.html')
    # handle lost connection
    except requests.exceptions.ConnectionError as errc:
        print(errc)
        return render(request, 'CloudOSAs2021/plotchart.html')
    # handle timeout wihout request
    except requests.exceptions.Timeout as errt:
        print(errt)
        return render(request, 'CloudOSAs2021/plotchart.html')


@csrf_exempt
def terminalquery(request):
    content = request.read()
    print(content)
    print(json.loads(content))
    c = json.loads(content)
    print(c['command'])
    try:
        r = requests.get('http://flaskosa.herokuapp.com'+c['command'])
        print("r.text")
        print(r.text)
        dump = json.dumps({
            'response': r.text
        })
        return HttpResponse(dump, content_type='application/json')
    # handle lost connection
    except requests.exceptions.ConnectionError as errc:
        print(errc)
        return HttpResponse(json.dumps({'response': "someerror"}), content_type='application/json')
    # handle timeout wihout request
    except requests.exceptions.Timeout as errt:
        print(errt)
        return HttpResponse(json.dumps({'response': "someerror"}), content_type='application/json')
    except SyntaxError as errs:
        print(errs)
        return HttpResponse(json.dumps({'response': "someerror"}), content_type='application/json')
