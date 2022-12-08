from rest_framework import serializers
from .models import Restaurant
from .models import Usera
from .models import Result
from .models import Comment


class RestaurantSerializers(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = "__all__"


class UseraSerializers(serializers.ModelSerializer):
    class Meta:
        model = Usera
        fields = "__all__"


class ResultSerializers(serializers.ModelSerializer):
    class Meta:
        model = Result
        fields = "__all__"


class CommentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"
