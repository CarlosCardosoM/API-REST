from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import Monografia
from .serializers import MonografiaSerializer
from rest_framework.permissions import AllowAny


@api_view(['GET', 'POST'])
@permission_classes([AllowAny])  # <=== ISSO LIBERA
def monografias_list(request):
    if request.method == 'GET':
        monografias = Monografia.objects.all()
        serializer = MonografiaSerializer(monografias, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        token_auth = TokenAuthentication()
        user_auth_tuple = token_auth.authenticate(request)
        if user_auth_tuple is None:
            return Response({'detail': 'Authentication credentials were not provided.'}, status=status.HTTP_401_UNAUTHORIZED)
        
        serializer = MonografiaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def monografia_detail(request, pk):
    try:
        monografia = Monografia.objects.get(pk=pk)
    except Monografia.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = MonografiaSerializer(monografia)
        return Response(serializer.data)

    elif request.method in ['PUT', 'PATCH']:
        partial = (request.method == 'PATCH')
        serializer = MonografiaSerializer(monografia, data=request.data, partial=partial)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        monografia.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)