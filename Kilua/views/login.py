from django.shortcuts import render
from Kilua.forms import *




def logar(request):
     # A HTTP POST?
    if request.method == 'POST':
        form = LoginForm(request.POST)


    else:
        # If the request was not a POST, display the form to enter details.
        form = LoginForm()

    # Bad form (or form details), no form supplied...
    # Render the form with error messages (if any).
    return render(request, 'login.html', {'form': form})
