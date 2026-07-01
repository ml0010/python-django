from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# requrst -> response


# Pull data from db
# Transform
# Send email...

def calculate():
   x = 1
   y = 1
   return x

def say_hello(request):
   x = calculate()
   return render(request, 'hello.html', {'name': 'Mimi'})  
   
   #return HttpResponse('Hello World')

   