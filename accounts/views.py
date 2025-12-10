from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

@login_required
def dashboard_redirect(request):
    # For now, just send everyone to home page; can later branch by role.
    return redirect("home")
