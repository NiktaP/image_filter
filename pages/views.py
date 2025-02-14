from django.core.files.storage import default_storage
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from test_djn import settings
from .serializer import Imageserializer
from .models import ImagesModels
import cv2,os
from django.core.files.base import ContentFile

MEDIA_ROOT = settings.MEDIA_ROOT
def gray(image_path):
    image= cv2.imread(image_path)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return gray_image



@api_view(['POST'])
def gray_filter(request):
    if 'image' in request.FILES:
        image_file = request.FILES['image']
        image_name = default_storage.save(image_file.name, ContentFile(image_file.read()))
        image_path = os.path.join(MEDIA_ROOT, image_name)

        converted_img = gray(image_path)
        converted_img_path=f'{os.path.splitext(image_path)[0]}_gray.jpg'
        cv2.imwrite(image_path,converted_img)

        image_instance = ImagesModels(image=image_file, new_image=image_path)
        image_instance.save()

        serializer = Imageserializer(image_instance)

        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response({'status': 'failure'}, status=status.HTTP_400_BAD_REQUEST)
