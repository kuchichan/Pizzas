from django.db import models


class Polling(models.Model):
    question_text = models.CharField(max_length=200)

    def __str__(self):
        return self.question_text


class Pizza(models.Model):
    polling = models.ForeignKey(Polling, on_delete=models.CASCADE)
    topping = models.CharField(max_length=200)
    topping_amount = models.IntegerField(default=10)
    votes = models.IntegerField(default=0)

    class Meta:
        ordering = ("id",)
        unique_together = ("polling", "topping")
