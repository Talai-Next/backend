from django.contrib import admin
from api.models import BusLocation, LineOneRoute, LineTwoRoute, LineThreeRoute, LineSpecialRoute

admin.register(BusLocation)
admin.register(LineOneRoute)
admin.register(LineTwoRoute)
admin.register(LineThreeRoute)
admin.register(LineSpecialRoute)
