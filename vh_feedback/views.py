from django.shortcuts import render, get_object_or_404
from .models import Feedback, FeedbackType
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from .serializers import *
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

import logging
logger = logging.getLogger(__name__)


class FeedbackView(generics.RetrieveAPIView):
    '''
    Получить процедуру по uid.
    '''
    serializer_class = FeedBackSerializer
    lookup_field = 'uid'
    def get_queryset(self):
        return Feedback.objects.all()

class FeedbackCreateView(generics.CreateAPIView):
    '''
    Сохранить обратную связь от пользователя
    '''
    serializer_class = FBCreateSerializer
    http_method_names = ['post']

    @swagger_auto_schema(request_body=FBCreateSerializer, responses={201: FeedBackSerializer, })
    def post(self, request, *args, **kwargs):
        serializer = FBCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        fb = Feedback(fb_type=get_object_or_404(FeedbackType, code='FeedBack'),
                      name=serializer.data['name'], email=serializer.data['email'],
                      phone=serializer.data['phone'], message=serializer.data['message'])
        fb.save()
        resSerializer = FeedBackSerializer(fb)
        # headers = self.get_success_headers(resSerializer.data)
        return Response(resSerializer.data, status=status.HTTP_201_CREATED)  # , headers=resSerializer.headers

class FeedbackCallCreateView(generics.CreateAPIView):
    '''
    Сохранить заказ на обратный звонок
    '''
    serializer_class = FBCallCreateSerializer
    http_method_names = ['post']

    @swagger_auto_schema(request_body=FBCallCreateSerializer, responses={201: FeedBackSerializer, })
    def post(self, request, *args, **kwargs):
        serializer = FBCallCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        fb = Feedback(fb_type=get_object_or_404(FeedbackType, code='FeedBackCall'), name=serializer.data['name'],
                      phone=serializer.data['phone'], call_hr=serializer.data['hr'], call_mn=serializer.data['min'])
        fb.save()
        resSerializer = FeedBackSerializer(fb)
        return Response(resSerializer.data, status=status.HTTP_201_CREATED)  # , headers=resSerializer.headers