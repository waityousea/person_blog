from django.contrib import admin
#model注册
from .models import Gallery

# Register your models here.

#注册model
admin.site.register(Gallery)