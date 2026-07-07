from django.shortcuts import render
from django.db.models import Q, F
from store.models import Product, OrderItem, Order, Customer
from django.db.models import Count, Max, Min, Avg, Sum
from django.db.models import Value, F, Func, Count, ExpressionWrapper, DecimalField
from django.db.models.functions import Concat

from django.contrib.contenttypes.models import ContentType
from store.models import Product, Collection


def say_hello(request):


   return render(request, 'hello.html', {'name': 'Mimi'})
   
 
   