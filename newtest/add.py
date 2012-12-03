from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import socket
import sys
import json

text = """<form method="post" action="/add/">
    <input type="text" name="a" value="%s"> + <input type="text" name="b" value="%s"> 
    <input type="submit" value="Score"> <input type="text" value="%s">
</form>"""

@csrf_exempt
def index(request):
    if request.POST.has_key('a'):

        a = request.POST['a']
        b = request.POST['b']
        c = ''
        data = a + " " + b
        data_string = json.dumps(data)
        c = data_string
        HOST, PORT = "localhost", 9999
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((HOST, PORT))
        sock.sendall(data_string + "\n")
        received = sock.recv(1024)
        sock.close()
        c = received
    else:
        a = ''
        b = ''
        c = ''
    return HttpResponse(text % (a, b, c))