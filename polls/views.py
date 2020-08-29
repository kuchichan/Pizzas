from django.shortcuts import render
from rest_framework import viewsets, status

from rest_framework.decorators import action
from rest_framework.response import Response

from polls.models import Polling, Pizza
from polls.serializers import PollingSerializer, PizzaSerializer


class PollingViewSet(viewsets.ModelViewSet):
    queryset = Polling.objects.all()
    serializer_class = PollingSerializer


class PizzaViewSet(viewsets.ModelViewSet):
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer

    @action(detail=True, methods=["patch"])
    def vote(self, request, pk=None):
        pizza = self.get_object()
        pizza.votes += 1
        pizza.save()

        return Response(status=status.HTTP_200_OK)
