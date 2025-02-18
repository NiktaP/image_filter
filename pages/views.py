from django.core.files.storage import default_storage
from django.http import HttpResponse
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

def blur(image_path):
    image=cv2.imread(image_path)
    blurred_image=cv2.blur(image,(15,15))
    return blurred_image
@api_view(['POST'])
def gray_filter(request):
    if 'image' in request.FILES:
        image_file = request.FILES['image']
        image_name = default_storage.save(image_file.name, ContentFile(image_file.read()))
        image_path = os.path.join(MEDIA_ROOT, image_name)

        converted_img = gray(image_path)
        converted_img_path=f'{os.path.splitext(image_path)[0]}_gray.jpg'
        cv2.imwrite(converted_img_path,converted_img)

        image_instance = ImagesModels(image=image_file, new_image=converted_img_path)
        image_instance.save()

        serializer = Imageserializer(image_instance)

        result , buffer = cv2.imencode('.jpg',converted_img)


        return HttpResponse(buffer.tobytes(), content_type='image/jpeg')
    return Response({'status': 'failure'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def blur_filter(request):
    if 'image' in request.FILES:
        image_file=request.FILES['image']
        image_name=default_storage.save(image_file.name,ContentFile(image_file.read()))
        image_path=os.path.join(MEDIA_ROOT,image_name)

        converted_img=blur(image_path)
        converted_img_path=f'{os.path.splitext(image_path)[0]}_blur.jpg'
        cv2.imwrite(converted_img_path,converted_img)

        image_instance= ImagesModels(image=image_file,new_image=converted_img_path)
        image_instance.save()

        serializer=Imageserializer(image_instance)

        result, buffer = cv2.imencode('.jpg', converted_img)

        return HttpResponse(buffer.tobytes(), content_type='image/jpeg')
    return Response({'status': 'failure'}, status=status.HTTP_400_BAD_REQUEST)