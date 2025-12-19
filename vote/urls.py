
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # 1. CORE VOTING VIEWS
    path('', views.home, name="home"), 
    path('results/', views.results, name='results'),
    
    # 🌟 ADDED: VOTE AND CANDIDATE URL NAMES 🌟
    path('cast-vote/', views.cast_vote, name='cast_vote'), 
    path('candidates/', views.candidate_list, name='candidate'), 
    
    # 2. CHATBOT / NEWS VIEWS
    path('news/', views.sa_politics_news, name='news'),
    path('chatbot/', views.chatbot_view, name='chatbot'),
    
    # 3. CUSTOM AUTHENTICATION VIEWS
    path('signup/', views.signup_view, name='signup'), 
    path('login/', views.login_view, name='login'), 
    path('logout/', views.logout_view, name='logout'),
]