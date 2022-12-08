from django.db import models


class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    rating = models.IntegerField()
    imageTitleUrls = models.CharField(max_length=1000)
    imageUrls = models.CharField(max_length=1000)
    timeWork = models.CharField(max_length=500)
    latitude = models.FloatField(max_length=100)
    longitude = models.FloatField(max_length=100)
    phone = models.CharField(max_length=11)

    def __str__(self):
        return f"{self.pk}_{self.name}"


class Usera(models.Model):
    name = models.CharField(max_length=100)
    family = models.CharField(max_length=100)
    userName = models.CharField(max_length=100, unique=True)
    phone = models.CharField(max_length=11)
    passWord = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.pk} _ {self.name}"


class Result(models.Model):
    guId = models.CharField(max_length=1000)
    any = models.JSONField(max_length=10000)
    status = models.CharField(max_length=1000)
    ip = models.CharField(max_length=1000)
    erorr = models.CharField(max_length=1000)

    def __str__(self):
        return f"{self.pk} _ {self.guId}"


class Comment(models.Model):
    userId = models.CharField(max_length=1000)
    username = models.CharField(max_length=1000)
    restaurantId = models.CharField(max_length=1000)
    comment = models.CharField(max_length=10000)

    def __str__(self):
        return f"{self.pk} _ {self.comment}"
