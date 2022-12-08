
from django.urls import path

from . import views

urlpatterns = [
    path('test', views.test, name='test'),
    path('showRestaurant', views.showRestaurant, name='showRestaurant'),
    path('addUser', views.addUser, name='addUser'),
    path('addComment', views.addComment, name='addComment'),
    path('showComment/<restaurantId>', views.showComment, name='showComment'),
    path('loginUser/<username>,<password>', views.loginUser, name='loginUser'),
    path('forgetPass/', views.forgetPass, name='forgetPass'),
]

