from .models import Document
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .serializers import DocumentSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response    
from rest_framework import viewsets 
from rest_framework.exceptions import ParseError
from rest_framework.parsers import FileUploadParser
from rest_framework.views import APIView
from rest_framework.decorators import permission_classes,authentication_classes,action
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication


class DocumentViewSet(viewsets.ModelViewSet):
    pass
#     authentication_classes=([TokenAuthentication,])
#     permission_classes=([IsAuthenticated,]) 
#     # @action(methods=['post'], detail=True)
#     # def documentList(req):


#     #     doc = Document.objects.filter(user=req.user)
#     serializer_class = DocumentSerializer
#     # queryset = Document.objects.all()
        

#     def get_queryset(self, *args, **kwargs):
#         return Document.objects.filter(user=self.request.user)





#Mine

@api_view(['GET'])
@authentication_classes([TokenAuthentication,])
@permission_classes([IsAuthenticated,]) 
def documentList(req):
    
    
    doc = Document.objects.filter(user=req.user)
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
    # breakpoint()
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)



