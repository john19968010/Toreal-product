from django.contrib import admin
from .models import Card, User

class UserA(admin.ModelAdmin):
    list_display = ('fullname' , 'gender' , 'age', 'county', 'email')
admin.site.register(User, UserA)

class CardA(admin.ModelAdmin):
    list_display = ('card_name' , 'card_msg' , 'card_url')
admin.site.register(Card, CardA)



