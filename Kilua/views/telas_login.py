from django.shortcuts import render


def controle_admin(request):
    return render(request, "controle.html")
