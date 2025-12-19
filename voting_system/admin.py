from django.contrib import admin
from django.contrib.auth.models import User
from vote import models
from .models import Leader, Candidate

@admin.register(Leader)
class LeaderAdmin(admin.ModelAdmin):
    list_display = ('name', 'party', 'date_of_birth')


@admin.register(Candidate)
class CandidateAdmin(admin.ModelAdmin):
    list_display = ('name', 'party')

from django.contrib import admin
from .models import Election

@admin.register(Election)
class ElectionAdmin(admin.ModelAdmin):
    list_display = ['name']
