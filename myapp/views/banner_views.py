from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from ..models import Banner
from ..serializers import BannerSerializers

#List
@api_view(['GET'])
def banner_list(request):
    banners = Banner.objects.all().order_by('-id')
    serializer = BannerSerializers(banners,many=True)
    return Response(serializer.data)


#create
@api_view(['POST'])
def banner_create(request):
    serializers = BannerSerializers(data=request.data)
    if serializers.is_valid():
        serializers.save()
        return Response(serializers.data, status=status.HTTP_201_CREATED)
    return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


#  Detail
@api_view(['GET'])
def banner_detail(request, pk):
    try:
        banner = Banner.objects.get(pk=pk)
    except Banner.DoesNotExist:
        return Response({'error': 'Banner not found'}, status=status.HTTP_404_NOT_FOUND)

    serializer = BannerSerializers(banner)
    return Response(serializer.data)

# delete
@api_view(['DELETE'])
def banner_delete(request, pk):
    try:
        banner = Banner.objects.get(pk=pk)
    except Banner.DoesNotExist:
        return Response({'error': 'Banner not found'}, status=status.HTTP_404_NOT_FOUND)
    banner.delete()
    return Response({'message':'Delete successfully'}, status=status.HTTP_204_NO_CONTENT)