from django.shortcuts import render
from django.http import HttpResponse

def add(request):
    n1 = 100
    n2 = 200
    n3 = n1 + n2
    
    output ='''
    <html>
    <body>
    <h2>Sum of {} and {} is = {} </h2>
    </body>
    </html>'''.format(n1,n2,n3)
    response = HttpResponse(output)
    return response
def sub(request):
    n1=200
    n2 = 100
    n3 = n1-n2
    output = '''
    <html><body>
    <h2>Diff of {} and {} is =  {}</h2>
    </body></html>'''.format(n1,n2,n3)
    response=HttpResponse(output)
    return response

