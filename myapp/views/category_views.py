from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from ..models import Category
from ..serializers import CategorySerializers

#List
@api_view(['GET'])
def category_list(request):
    categories = Category.objects.all().order_by('-id')
    serializer = CategorySerializers(categories,many=True)
    return Response(serializer.data)

#create
@api_view(['POST'])
def category_create(request):
    serializers = CategorySerializers(data=request.data)
    if serializers.is_valid():
        serializers.save()
        return Response(serializers.data, status=status.HTTP_201_CREATED)
    return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

#  Detail
@api_view(['GET'])
def category_detail(request, pk):
    try:
        category = Category.objects.get(pk=pk)
    except Category.DoesNotExist:
        return Response({'error': 'Category not found'}, status=status.HTTP_404_NOT_FOUND)

    serializer = CategorySerializers(category)
    return Response(serializer.data)

# delete
@api_view(['DELETE'])
def category_delete(request, pk):
    try:
        category = Category.objects.get(pk=pk)
    except Category.DoesNotExist:
        return Response({'error': 'Category not found'}, status=status.HTTP_404_NOT_FOUND)
    category.delete()
    return Response({'message':'Delete successfully'}, status=status.HTTP_204_NO_CONTENT)


# Update (PUT + PATCH)
@api_view(['PUT', 'PATCH'])
def category_update(request, pk):
    try:
        category = Category.objects.get(pk=pk)
    except Category.DoesNotExist:
        return Response({'error': 'Category not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = CategorySerializers(category, data=request.data)
    else: #PATCH
        serializer = CategorySerializers(Category, data=request.data, partial=True)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)