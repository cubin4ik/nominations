from django.contrib import admin
from .models import Nominations, Votes

admin.site.register(Votes)
admin.site.register(Nominations)
