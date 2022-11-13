from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Jobs_db
from .serializers import *



@api_view(['GET', 'POST'])
def jobsdb_list(request):

    if request.method == 'GET':
    
        q = request.GET.get('q', None)
                
        if q != None:
            queryset = Jobs_db.objects.filter(title__icontains=q).order_by('id')
        
            page = request.GET.get('page', 1)
            
            paginator = Paginator(queryset, 100)
            
            data = []           

            try:
                data = paginator.page(page)
            except PageNotAnInteger:
                data = paginator.page(1)
            except EmptyPage:
                data = paginator.page(paginator.num_pages)

            serializer = JobsDbSerializer(data,context={'request': request} ,many=True)

            context = {'jobsdb': serializer.data , 
                        'count': paginator.count,
                        'number': data.number,
                       'numpages' : paginator.num_pages, 
                       
                       }
            return Response(context)            
            
        data = []
        nextPage = 1
        previousPage = 1
        
        items = Jobs_db.objects.all()
        page = request.GET.get('page', 1)
        paginator = Paginator(items, 100)
        try:
            data = paginator.page(page)
        except PageNotAnInteger:
            data = paginator.page(1)
        except EmptyPage:
            data = paginator.page(paginator.num_pages)

        serializer = JobsDbSerializer(data,context={'request': request} ,many=True)

        context = {'jobsdb': serializer.data , 
                    'count': paginator.count,
                    'number': data.number,
                   'numpages' : paginator.num_pages, 
                   
                   }
        return Response(context)

    elif request.method == 'POST':
        serializer = JobsDbSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        
@api_view(['GET', 'PUT', 'DELETE'])
def jobsdb_detail(request, pk):
    try:
        items = Jobs_db.objects.get(pk=pk)
    except Jobs_db.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = JobsDbSerializer(items,context={'request': request})
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = JobsDbSerializer(items, data=request.data,context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        items.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)        
