# main/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='main_home'),
    path('login/', views.login_view, name='main_login'),
    path('signup/', views.signup_view, name='main_signup'),
    path('vote/', views.vote_view, name='main_vote'),
    path('results/', views.results_view, name='main_results'),
    path('biometric/', views.biometric_verify, name='main_biometric'),
    path('logout/', views.logout_view, name='main_logout'),  # <-- added
    path('terms/', views.terms, name='main_terms'),
]
