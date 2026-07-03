from django.shortcuts import render
from django.http import HttpResponse
from store.models import Product
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.
# requrst -> response


# Pull data from db
# Transform
# Send email...


def say_hello(request):
   #queryset = Product.objects.filter(unit_price__range=(20, 30))
   #queryset = Product.objects.filter(collection__id__range=(1, 2, 3))
   #queryset = Product.objects.filter(title__icontains='coffee')
   #queryset = Product.objects.filter(last_update__year=2021)
   queryset = Product.objects.filter(description__isnull=True)

   return render(request, 'hello.html', {'name': 'Mimi', 'products': list(queryset)})
   
   #return HttpResponse('Hello World')

   