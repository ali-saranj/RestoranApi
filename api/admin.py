from django.contrib import admin
from .models import Restaurant
from .models import Usera
from .models import Result
from .models import Comment

# Register your models here.
admin.site.register(Restaurant)
admin.site.register(Usera)
admin.site.register(Result)
admin.site.register(Comment)
