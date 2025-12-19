from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib import messages

# Import vote app views to delegate where appropriate
from vote import views as vote_views


def home(request):
    """Delegate to vote.home_view if available (keeps single source of truth)."""
    return vote_views.home_view(request)


def login_view(request):
    """Delegate login handling to `vote.views.login_view`."""
    return vote_views.login_view(request)


def signup_view(request):
    """Lightweight signup placeholder.

    This project doesn't currently have a full signup flow. Show a simple
    signup page that links to login. If you prefer, we can wire a real
    registration flow using `django.contrib.auth.forms.UserCreationForm`.
    """
    if request.method == 'POST':
        # Minimal behaviour: redirect to login and show a message (no user created)
        messages.info(request, 'Signup is not implemented; please contact admin or use the admin panel to create users.')
        return redirect('login')
    return render(request, 'main/signup.html')


def vote_view(request):
    """Route to the vote/news page (keeps legacy vote routes simple)."""
    return redirect('news')


def results_view(request):
    """Delegate to vote.views.results_view to show results."""
    return vote_views.results_view(request)


def biometric_verify(request):
    """Placeholder biometric verification page (not implemented).

    Replace this with an actual verification integration when available.
    """
    return render(request, 'main/biometric.html')


def terms(request):
    """Render the Terms & Conditions page."""
    return render(request, 'main/terms.html')


def logout_view(request):
    """
    Logs the user out (POST) and shows a logout confirmation page.
    If request method is GET we show the confirmation page with a POST form.
    """
    if request.method == "POST":
        logout(request)
        messages.success(request, "You have been logged out.")
        return render(request, 'main/logout.html', {'just_logged_out': True})

    # GET: show confirmation page asking user to confirm logout
    return render(request, 'main/logout.html', {'just_logged_out': False})
