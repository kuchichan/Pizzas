from django.shortcuts import render
from rest_framework import viewsets

from polls.models import Polling, Pizza
from polls.serializers import PollingSerializer, PizzaSerializer


class PollingViewSet(viewsets.ModelViewSet):
    queryset = Polling.objects.all()
    serializer_class = PollingSerializer


class PizzaViewSet(viewsets.ModelViewSet):
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer
