from django.shortcuts import render
from Kilua.forms import *

def controle_admin(request):
    return render(request, "admin_controle.html")
