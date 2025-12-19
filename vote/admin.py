from django.contrib import admin
from .models import Leader, Candidate   # import both models
from .models import Election, Candidate, Voter, Vote

from django.contrib import admin
from .models import Leader, Candidate, Election, Voter, Vote

@admin.register(Leader)
class LeaderAdmin(admin.ModelAdmin):
    list_display = ('name', 'party', 'website')
    search_fields = ('name', 'party', 'website')

@admin.register(Candidate)
class CandidateAdmin(admin.ModelAdmin):
    list_display = ('name', 'party', 'election')  # combine what you need
    search_fields = ('name', 'party')

@admin.register(Election)
class ElectionAdmin(admin.ModelAdmin):
    list_display = ('name', 'date')

@admin.register(Voter)
class VoterAdmin(admin.ModelAdmin):
    list_display = ('user', 'has_voted')  # use the correct field name


@admin.register(Vote)
class VoteAdmin(admin.ModelAdmin):
    list_display = ('voter', 'candidate', 'election', 'timestamp')
