from rest_framework import serializers

from polls.models import Polling, Pizza


class PollingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Polling
        fields = ("id", "question_text")


class PizzaSerializer(serializers.ModelSerializer):
    votes = serializers.ReadOnlyField()

    class Meta:
        model = Pizza
        fields = ("id", "polling", "topping", "votes")
