from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView

from .models import Crud
from .serializer import CrudSerializer


class ListCrudAPIView(ListAPIView):
    """ get cruds """
    queryset = Crud.objects.all()
    serializer_class = CrudSerializer


class CreateCrudAPIVeiw(CreateAPIView):
    """ post crud"""
    queryset = Crud.objects.all()
    serializer_class = CrudSerializer


class UpdateCrudAPIView(UpdateAPIView):
    """ put crud """
    queryset = Crud.objects.all()
    serializer_class = CrudSerializer


class DeleteCrudAPIView(DestroyAPIView):
    """ delete crud """
    queryset = Crud.objects.all()
    serializer_class = CrudSerializer
