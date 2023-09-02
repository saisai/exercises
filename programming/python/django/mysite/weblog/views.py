import json

from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser



from rest_framework.response import Response
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import TemplateHTMLRenderer

from rest_framework import status

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


from .models import Blog, Author
from .serializers import *

def index(request):
    context = {}
    return render(request, 'weblog/weblog.html', context=context)

@api_view(['GET', 'POST'])
def weblog_test(request):

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

    context = {'data': serializer.data,
               'count': paginator.count,
               'msg': '',
               'code': 0,

               }

    return Response(context)


def author(request):
    context = {}
    return render(request, 'weblog/author.html', context=context)

@api_view(['GET', 'POST'])
def author_test(request):
    items = Author.objects.all().order_by('id')
    page = request.GET.get('page', 1)
    limit = request.GET.get('limit', 10)
    paginator = Paginator(items, limit)
    try:
        data = paginator.page(page)
    except PageNotAnInteger:
        data = paginator.page(1)
    except EmptyPage:
        data = paginator.page(paginator.num_pages)

    serializer = AuthorSerializer(data, context={'request': request}, many=True)

    context = {'data': serializer.data,
               'count': paginator.count,
               'msg': '',
               'code': 0,
               }
    return Response(context)

@api_view(['GET', 'POST'])
def author_delete(request):
    #print(request.data)
    ids = list(map(int, request.POST.getlist('id[]') ))

    for id in ids:
        Author.objects.filter(pk=id).delete()

    return Response({'success': True})

@api_view(['GET', 'POST'])
@renderer_classes([TemplateHTMLRenderer])
def author_add(request):
    if request.method == 'GET':
        print('add')
        return Response(template_name='weblog/add_author.html')
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = serializers.AuthorSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.data, status=400)

@csrf_exempt
@api_view(['GET', 'POST'])
def add_author(request):
    if request.method == 'GET':
        print('get')
    elif request.method == 'POST':
        print('post', request)
        print(request.POST)
        print(request.data)
        print(request.POST)
        #data = JSONParser().parse(request)
        #print(data)
        serializer = AuthorSerializer(data=request.POST)
        print(serializer)
        if serializer.is_valid():
            print('valid')
            serializer.save()
            data_response = {'status': "success", 'msg':'Success'}
            return JsonResponse(data_response, status=200)
            #return JsonResponse(serializer.data, status=200)
        #return JsonResponse(serializer.data, status=400)
        data_response = {'status': "error", 'msg': 'Error'}
        return JsonResponse(serializer.data, status=400)
