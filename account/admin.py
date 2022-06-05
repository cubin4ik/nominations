from django.contrib import admin
from .models import User
from votes.models import Votes, Nominations


class VotesInline(admin.TabularInline):
    model = Votes
    extra = 0
    fk_name = 'voter'


class UserAdmin(admin.ModelAdmin):
    inlines = [VotesInline]


admin.site.register(User, UserAdmin)
