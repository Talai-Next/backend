from django.contrib import admin
from api.models import StationLocation, LineOneRoute, LineFiveRoute, LineThreeRoute, LineSpecialRoute

# Register your models here.

admin.site.register(StationLocation)
admin.site.register(LineOneRoute)
admin.site.register(LineFiveRoute)
admin.site.register(LineThreeRoute)
admin.site.register(LineSpecialRoute)
