from django.contrib import admin

from app.models import Reservation, Room, TypeRoom

admin.site.register(Room)
admin.site.register(Reservation)
admin.site.register(TypeRoom)
# Register your models here.
