from django.contrib import admin
from api.models import BusLocation, LineOneRoute, LineTwoRoute, LineThreeRoute, LineSpecialRoute

# Register your models here.

admin.site.register(BusLocation)
admin.site.register(LineOneRoute)
admin.site.register(LineTwoRoute)
admin.site.register(LineThreeRoute)
admin.site.register(LineSpecialRoute)
