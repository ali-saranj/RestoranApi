from django.shortcuts import render
from django.http.response import JsonResponse, HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Restaurant
from .serializers import RestaurantSerializers
from .models import Usera
from .models import Comment
from .models import Result
from .serializers import UseraSerializers
from .serializers import ResultSerializers
from .serializers import CommentSerializers
import uuid


@api_view(['GET'])
def test(request):
    name = "ali"
    user = Usera.objects.all()
    data = {
        "name": "ali2",
        "family": "sarang",
        "userName": "alisaaasdfda",
        "passWord": "3414134233"
    }
    selUser = UseraSerializers(data=data)
    if selUser.is_valid():
        selUser.save()
    return Response(selUser.data)


@api_view(['POST'])
def addUser(request):
    data = dict(request.data)
    print(data)

    try:
        user = Usera.objects.get(userName=data["userName"])
        selUser = UseraSerializers(user, many=False)
        dataResult = {
            "guId": str(uuid.uuid4()),
            "any": {"User": "null"},
            "status": "Cansel",
            "ip": str(request.META['REMOTE_ADDR']),
            "erorr": "user is exist"
        }
        selResult = ResultSerializers(data=dataResult)
        if selResult.is_valid():
            selResult.save()
        return Response(selResult.data)
    except Exception:
        sel2 = UseraSerializers(data=request.data)
        if sel2.is_valid():
            sel2.save()
            dataResult = {
                "guId": str(uuid.uuid4()),
                "any": {"User": dict(sel2.data)},
                "status": "OK",
                "ip": str(request.META['REMOTE_ADDR']),
                "erorr": "NUll"
            }
            selResult1 = ResultSerializers(data=dataResult)
            if selResult1.is_valid():
                selResult1.save()
            return Response(selResult1.data)


@api_view(["GET"])
def loginUser(request, username, password):
    try:
        user = Usera.objects.get(userName=username)
        seluser = UseraSerializers(user, many=False)

        if seluser.data["passWord"] == password:
            dataResult = {
                "guId": str(uuid.uuid4()),
                "any": {"User": dict(seluser.data)},
                "status": "OK",
                "ip": str(request.META['REMOTE_ADDR']),
                "erorr": "NUll"
            }
            selResult = ResultSerializers(data=dataResult)
            if selResult.is_valid():
                selResult.save()
            return Response(selResult.data)
        else:
            dataResult = {
                "guId": str(uuid.uuid4()),
                "any": {"User": "Null"},
                "status": "OK",
                "ip": str(request.META['REMOTE_ADDR']),
                "erorr": "Password is false"
            }
            selResult = ResultSerializers(data=dataResult)
            if selResult.is_valid():
                selResult.save()
            return Response(selResult.data)
    except Exception:
        dataResult1 = {
            "guId": str(uuid.uuid4()),
            "any": {"User": "null"},
            "status": "Cansel",
            "ip": str(request.META['REMOTE_ADDR']),
            "erorr": "user is not exist"
        }
        selResult1 = ResultSerializers(data=dataResult1)
        if selResult1.is_valid():
            selResult1.save()
        return Response(selResult1.data)


@api_view(["POST"])
def forgetPass(request):
    result = 0
    try:
        phone = request.META["HTTP_PHONE"]
        user = Usera.objects.get(phone=phone)
        seluser = UseraSerializers(user,many=False)
        dataResult = {
            "guId": str(uuid.uuid4()),
            "any": {"user": dict(seluser.data)},
            "status": "OK",
            "ip": str(request.META['REMOTE_ADDR']),
            "erorr": "NUll"
        }
        result = ResultSerializers(data=dataResult)
        if result.is_valid():
            result.save()
    except Exception as e:
        dataResult = {
            "guId": str(uuid.uuid4()),
            "any":"null",
            "status": "Cansel",
            "ip": str(request.META['REMOTE_ADDR']),
            "erorr": str(e)
        }
        result = ResultSerializers(data=dataResult)
        if result.is_valid():
            result.save()

    return Response(result.data)

@api_view(["POST"])
def addComment(request):
    data = dict(request.data)
    print(data)

    selcom = CommentSerializers(data=request.data)
    if selcom.is_valid():
        selcom.save()
        dataResult = {
            "guId": str(uuid.uuid4()),
            "any": {"Comment": dict(selcom.data)},
            "status": "OK",
            "ip": str(request.META['REMOTE_ADDR']),
            "erorr": "NUll"
        }
        selris = ResultSerializers(data=dataResult)
        if selris.is_valid():
            selris.save()
        return Response(selris.data)
    else:
        dataResult = {
            "guId": str(uuid.uuid4()),
            "any": {"Comment": "Null"},
            "status": "Cansel",
            "ip": str(request.META['REMOTE_ADDR']),
            "erorr": "can not add comment"
        }
        selris = ResultSerializers(data=dataResult)
        if selris.is_valid():
            selris.save()
        return Response(selris.data)


@api_view(["GET"])
def showComment(request, restaurantId):
    print(restaurantId)
    coments = Comment.objects.all().filter(restaurantId=restaurantId)
    sele = CommentSerializers(coments, many=True)
    return Response(sele.data)


@api_view(["GET"])
def showRestaurant(request):
    restorans = Restaurant.objects.all()
    sele = RestaurantSerializers(restorans, many=True)
    return Response(sele.data)
