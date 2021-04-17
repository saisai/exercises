import json

from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers


from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


from .models import Blog
from .serializers import *

def index(request):
    context = {}
    return render(request, 'weblog/weblog.html', context=context)

@api_view(['GET', 'POST'])
def weblog_test(request):
    obj = Blog.objects.all().values()

    data = []
    nextPage = 1
    previousPage = 1

    items = Blog.objects.all().order_by('id')
    page = request.GET.get('page', 1)
    limit = request.GET.get('limit', 10)
    paginator = Paginator(items, limit)
    try:
        data = paginator.page(page)
    except PageNotAnInteger:
        data = paginator.page(1)
    except EmptyPage:
        data = paginator.page(paginator.num_pages)

    serializer = BlogSerializer(data, context={'request': request}, many=True)

    """
    context = {'data': serializer.data , 
                'count': paginator.count,
                'count': data.number,
               'numpages' : paginator.num_pages, 

               }
    """
    context = {'data': serializer.data,
               'count': paginator.count,
               'msg': '',
               'code': 0,

               }

    return Response(context)

    """
    qs_json = serializers.serialize('json', obj)

    print(type(qs_json))

    to_json = json.loads(qs_json)

    print(type(to_json))
    print(to_json[0].get('fields'))
    print(type(to_json[0].get('fields')))
    print(qs_json)
    
    #print(obj)
    
    json_obj = []
    for result in obj:
        #print(result)
        json_obj.append(result)
    context = {
        'code': 0,
        'msg': "",
        'count': obj.count(),
        'data': json_obj
    }



    return JsonResponse(context, content_type='application/json')
    """