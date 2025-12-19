from django.shortcuts import render
from vote.models import Leader

def sa_politics_news(request):
    leaders = Leader.objects.all()
    return render(request, 'vote/sa_news.html', {'leaders': leaders})

def chatbot_page(request):
    if request.method == "POST":
        message = request.POST.get("message")
        # handle message here
    return render(request, "chatbot.html")
