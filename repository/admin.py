from django.contrib import admin
from .models import Photo, HistoryConnection, ProfileUser
# Register your models here.
admin.site.register(Photo)
admin.site.register(HistoryConnection)
admin.site.register(ProfileUser)
