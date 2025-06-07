from django.contrib import admin

# from app.models
class reservationAdmin(admin.ModelAdmin):
    list_display =('room, 'date_start', 'phone')
    search_fileds = ('room', 'date')

admin.site.register(Room)
admin.site.register(Reservation)
admin.site.register(TypeRoom)

