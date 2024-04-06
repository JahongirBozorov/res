from django.contrib import admin

from restaurant_app.models import *
from user.models import MyUser

# Register your models here.
admin.site.register(MyUser)

# Register your models here.
from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin


admin.site.register(Restaurant)
admin.site.register(Food)
admin.site.register(Restaurant_comment)
admin.site.register(Restaurant_location)
admin.site.register(Food_comment)

