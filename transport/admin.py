from django.contrib import admin
from .models import Driver, BusIncharge, BusRoute, BoardingPoint, Student, BusApplication

admin.site.register(Driver)
admin.site.register(BusIncharge)
admin.site.register(BusRoute)
admin.site.register(BoardingPoint)
admin.site.register(Student)
admin.site.register(BusApplication)
