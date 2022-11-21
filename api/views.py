from django.shortcuts import render
from rest_framework.response import Response
from .models import Note

from .serializers.serializers import NoteSerializer

from rest_framework.decorators import api_view
# Create your views here.


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def test(request):

    if request.method == 'GET':
        print('get')
        return Response({'test':'get'})

    if request.method == 'POSt':
        return Response({'test':'post'})


    if request.method == 'PUT':
        return Response({'test':'PUT'})

    if request.method == 'DELETE':
        return Response({'test':'delete'})


@api_view(['GET'])
def getNotes(request):
    notes = Note.objects.all()
    serializer = NoteSerializer(notes, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getNote(request, pk):
    notes = Note.objects.get(id=pk)
    serializer = NoteSerializer(notes, many=False)
    return Response(serializer.data)