from .models import Document
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .serializers import DocumentSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response     



@api_view(['GET'])
def documentList(req):
    doc = Document.objects.all()
    serializer = DocumentSerializer(doc, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def documentDetailList(req, pk):
    doc = Document.objects.get(id=pk)
    serializer = DocumentSerializer(doc, many = False)
    return Response(serializer.data)


@api_view(['POST'])
def documentCreate(req):
    serializer = DocumentSerializer(data=req.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
