# vote/models.py - CLEANED AND MERGED VERSION

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone # Import for default date/time values

# --- 1. LEADER MODEL (Party/Biography info) ---
class Leader(models.Model):
    name = models.CharField(max_length=100)
    party = models.CharField(max_length=100)
    biography = models.TextField(blank=True, null=True)
    community_contribution = models.TextField(blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='leaders/', blank=True, null=True)
    website = models.URLField(max_length=200, blank=True, null=True) # Added null=True for safety
    
    # Required for the LeaderAdmin E108 check in your previous error
    position = models.CharField(max_length=1000, default="President")
    votes = models.IntegerField(default=0) 

    def __str__(self):
        return self.name

# --- 2. ELECTION MODEL ---
class Election(models.Model):
    ELECTION_CHOICES = [
        ('national', 'National Elections'),
        ('local', 'Local Elections'), # Added from your second block
    ]
    name = models.CharField(max_length=200, choices=ELECTION_CHOICES)
    # Required for the ElectionAdmin E108 check in your previous error
    date = models.DateField(default=timezone.now) 
    
    # Added from your second block
    title = models.CharField(max_length=200, default='General Election')
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

# --- 3. POSITION MODEL ---
class Position(models.Model):
    name = models.CharField(max_length=100)
    # Ensure this ForeignKey is correct
    election = models.ForeignKey(Election, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.name} ({self.election.name if self.election else 'N/A'})"


# --- 4. CANDIDATE MODEL ---
class Candidate(models.Model):
    name = models.CharField(max_length=200)
    party = models.CharField(max_length=100, blank=True, null=True)
    election = models.ForeignKey(Election, on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='candidates/images/', blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.party})"

# --- 5. VOTER MODEL ---
class Voter(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    has_voted = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

# --- 6. VOTE MODEL ---
class Vote(models.Model):
    voter = models.ForeignKey(Voter, on_delete=models.CASCADE)
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    election = models.ForeignKey(Election, on_delete=models.CASCADE)
    # Using 'timestamp' for consistency with Admin E108 check
    timestamp = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return f"{self.voter.user.username} voted for {self.candidate.name}"